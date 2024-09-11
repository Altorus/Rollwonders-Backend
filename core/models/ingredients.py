from django.db import models


class IngredientCategory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=256)
    photo = models.FileField(verbose_name="Изображение", upload_to="photos/", null=True, blank=True)
    is_seasonal = models.BooleanField(verbose_name="Сезонное", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория ингридиентов"
        verbose_name_plural = "Категории ингридиентов"


class Ingredient(models.Model):
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE, related_name="ingredients", null=True, blank=True)
    name = models.CharField(verbose_name="Название", max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ингридиент"
        verbose_name_plural = "Ингридиенты"
