from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'authentication', views.LoginViewSet, basename='authentication')

routers = [
    *router.urls,
]

urlpatterns = [
    path("generate-recipe/", views.GenerateRecipeApiView.as_view(), name="generate_recipe"),
    path("generate-recipe/<int:pk>/", views.GenerateRecipeApiView.as_view(), name="generate_recipe"),
    *router.urls
]
