from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from core.models import Ingredient

User = get_user_model()


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="recipes")
    name = models.CharField(verbose_name="Название", max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:recipe_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"



class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Ингридиент"
        verbose_name_plural = "Ингридиенты"


class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="steps")
    text = models.TextField()

    class Meta:
        verbose_name = "Шаг"
        verbose_name_plural = "Шаги"
        ordering = ('id',)
