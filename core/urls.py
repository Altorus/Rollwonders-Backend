from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('make-recipe/', views.MakeRecipeView.as_view(), name="make_recipe"),
    path('making-recipe/', views.MakingView.as_view(), name="making_recipe"),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name="recipe_detail"),
]
