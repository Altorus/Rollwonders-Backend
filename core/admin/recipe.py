from django.contrib import admin

from core import models


class IngredientInline(admin.StackedInline):
    model = models.RecipeIngredient
    extra = 1


class StepInline(admin.StackedInline):
    model = models.RecipeStep
    extra = 1


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientInline, StepInline)
