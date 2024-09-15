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
        recipe_name_pattern = r"\*\*Название:?\*\*\s*(.+?)\s*\*\*Ингредиенты:?\*\*"
        recipe_name_match = re.search(recipe_name_pattern, recipe_text)

        if not recipe_name_match:
            raise ValueError("Не найдено название рецепта")

        recipe_name = recipe_name_match.group(1).strip()

        # 2. Создание объекта Recipe
        recipe.name = recipe_name
        recipe.save()

        # 3. Парсинг ингредиентов
        ingredients_pattern = r"\*\*Ингредиенты:?\*\*([\s\S]+?)\*\*Этапы:?\*\*"
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
        steps_pattern = r"\*\*Этапы:?\*\*([\s\S]+)"
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

        # clean_result = "**Название:** Свинина с рисом и овощами **Ингредиенты:** 1. Свинина (500 г) 2. Рис (200 г) 3. Помидоры (2 шт.) 4. Груши (1 шт.) 5. Грейпфрут (1 шт.) 6. Укроп (по желанию) 7. Листовой салат (по желанию) 8. Соль (по вкусу) 9. Перец (по вкусу) 10. Оливковое масло (2 ст. ложки) **Этапы:** 1. Промойте рис под холодной водой и замочите его на 30 минут. После этого откиньте на дуршлаг. 2. Свинину нарежьте кубиками, посолите и поперчите по вкусу. Обжарьте мясо на сковороде с разогретым оливковым маслом до золотистой корочки. 3. Пока свинина жарится, нарежьте помидоры и грушу кубиками. Добавьте их к мясу, когда оно почти готово, и потушите ещё 5–7 минут, чтобы овощи стали мягкими. 4. В отдельной кастрюле отварите рис в подсоленной воде до готовности (примерно 15-20 минут). После приготовления слейте остатки воды. 5. Смешайте готовый рис с тушеной свининой и овощами. Перемешайте, добавьте мелко нарезанный укроп по желанию. 6. Грейпрут почистите и нарежьте на дольки. Подавайте нарезанный грейпрут вместе с рисом и свининой — это добавит интересного контраста вкусов. 7. Для подачи на тарелке добавьте листовой салат как гарнир. Приятного аппетита!"
        try:
            self.__parse_result(clean_result, recipe)
        except ValueError as e:
            logger.error(e)
