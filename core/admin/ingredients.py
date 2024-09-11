from django.contrib import admin

from core import models


class IngredientInline(admin.StackedInline):
    model = models.Ingredient
    extra = 1


@admin.register(models.IngredientCategory)
class IngredientCategoryAdmin(admin.ModelAdmin):
    inlines = (IngredientInline,)
