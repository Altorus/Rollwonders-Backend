from _project_.celery import app
from . import methods
from core import models


@app.task()
def generate_recipe_task(products: list, recipe_id: int):
    try:
        recipe = models.Recipe.objects.get(id=recipe_id)
        gpt_generator = methods.GPTGenerator()
        gpt_generator.generate_recipe(products, recipe)
    except models.Recipe.DoesNotExist:
        raise ValueError(f"Recipe with id {recipe_id} not found.")
