from django.views import generic

from core import models
from integrations.chat_gpt.methods import GPTGenerator


class IndexView(generic.TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # GPTGenerator().generate_recipe(['Макароны', "Бекон", "Сливки"])

        return context


class MakeRecipeView(generic.TemplateView):
    template_name = "pages/make_recipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            "season_categories": models.IngredientCategory.objects.filter(is_seasonal=True),
            "categories": models.IngredientCategory.objects.filter(is_seasonal=False),
        })

        return context


class RecipeDetailView(generic.DetailView):
    model = models.Recipe
    template_name = "pages/recipe.html"


class MakingView(generic.TemplateView):
    template_name = "pages/making-recipe.html"
