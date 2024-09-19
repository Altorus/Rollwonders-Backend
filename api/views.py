import pdb

from django.contrib.auth import login as auth_login
from django.contrib.auth.models import AnonymousUser
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from accounts.models import User
from core.models import Recipe
from .serializers import MakeRecipeSerializer, UserSerializer
from integrations.chat_gpt.tasks import generate_recipe_task

import logging

logger = logging.getLogger(__name__)


class GenerateRecipeApiView(CreateAPIView, RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MakeRecipeSerializer
    model = Recipe
    queryset = Recipe.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = super().retrieve(request, *args, **kwargs)
        recipe = self.get_object()
        if instance.status_code == 200 and recipe.steps.exists():
            return Response(data={"recipeCreated": True}, status=status.HTTP_200_OK)
        else:
            return Response(data={"recipeCreated": False}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a post object",
        request_body=MakeRecipeSerializer(),
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        recipe = serializer.save()
        ingredients = [ingredient.name for ingredient in serializer.validated_data['ingredients']]
        generate_recipe_task.delay(ingredients, recipe.id)

        return Response(data={"recipe_id": recipe.id}, status=status.HTTP_200_OK)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'telegram_id': openapi.Schema(type=openapi.TYPE_STRING, description='Telegram id'),
            },
            required=['name']
        ),
    )
    @action(methods=['POST'], detail=False, )
    def login(self, request, *args, **kwargs):
        try:
            user = User.objects.get(telegram_id=request.data['telegram_id'])
            auth_login(request, user)
            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=UserSerializer(),
    )
    @action(methods=['POST'], detail=False, )
    def register(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        auth_login(request, user)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=False, url_path='get-status')
    def get_status(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK, data={"status": request.user != AnonymousUser()})
