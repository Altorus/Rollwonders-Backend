import logging
import re
import requests
from django.db import transaction
from openai import OpenAI
from core import models
from . import constants
import environ
import os
from django.conf import settings as django_settings

environ.Env.read_env(os.path.join(django_settings.BASE_DIR, '.env'))
env = environ.Env()
logger = logging.getLogger('gpt')


class GPTGenerator:
    def __init__(self):
        self.__request_manager()

    def __request_manager(self):
        self._request_manager = requests.Session()

    @staticmethod
    def __get_prompt(products):
        product_list = ', '.join(products)
        prompt = constants.PROMPT.format(product_list)
        return re.sub(r'\s+', ' ', prompt).strip()

    @staticmethod
    @transaction.atomic
    def __parse_result(recipe_text: str, recipe: models.Recipe):
        # 1. Парсинг названия
        recipe_name_pattern = r"\*\*Название\*\* (.+?) \*\*Ингредиенты\*\*"
        recipe_name_match = re.search(recipe_name_pattern, recipe_text)

        logger.error(recipe_text)
        logger.error(recipe_name_match)

        if not recipe_name_match:
            raise ValueError("Не найдено название рецепта")

        recipe_name = recipe_name_match.group(1).strip()

        # 2. Создание объекта Recipe
        recipe.name = recipe_name
        recipe.save()

        # 3. Парсинг ингредиентов
        ingredients_pattern = r"\*\*Ингредиенты\*\*([\s\S]+?)\*\*Этапы\*\*"
        ingredients_match = re.search(ingredients_pattern, recipe_text)
        if not ingredients_match:
            raise ValueError("Не найдены ингредиенты")

        ingredients_block = ingredients_match.group(1).strip()

        # Разбиваем по строкам и парсим ингредиенты
        ingredient_lines = re.findall(r'\d+\.\s+(.+?)\((.+?)\)', ingredients_block)
        for ingredient_name, quantity in ingredient_lines:
            ingredient_name = ingredient_name.strip()
            quantity = quantity.strip()

            # Здесь предполагаем, что ингредиент уже есть в базе данных
            ingredient_obj = models.Ingredient.objects.get_or_create(name=ingredient_name)[0]

            # Создание объекта RecipeIngredient
            models.RecipeIngredient.objects.create(
                recipe=recipe,
                ingredient=ingredient_obj,
                quantity=quantity
            )

        # 4. Парсинг шагов рецепта
        steps_pattern = r"\*\*Этапы\*\*([\s\S]+)"
        steps_match = re.search(steps_pattern, recipe_text)
        if not steps_match:
            raise ValueError("Не найдены этапы приготовления")

        steps_block = steps_match.group(1).strip()

        # Разбиваем шаги по порядковым номерам
        step_lines = re.findall(r'\d+\.\s+(.+?)(?=\d+\.|$)', steps_block, re.DOTALL)
        for step_text in step_lines:
            step_text = step_text.strip()

            # Создание объекта RecipeStep
            models.RecipeStep.objects.create(
                recipe=recipe,
                text=step_text
            )

        return recipe

    def generate_recipe(self, products: list, recipe: models.Recipe):
        client = OpenAI(
            api_key=env("GPT_TOKEN"),
            organization='org-3cbCgaEqON5TcNPvqZSHkl4n',
            project='proj_aDspcNxkZ4fPTcl2JaSlVlJA',
        )
        prompt = self.__get_prompt(products)

        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        result = stream.choices[0].message.content
        clean_result = re.sub(r'\s+', ' ', result).strip()
        logger.error(clean_result)
        try:
            self.__parse_result(clean_result, recipe)
        except ValueError as e:
            logger.error(e)
