from rest_framework import serializers
from core import models
from accounts import models as account_models


class MakeRecipeSerializer(serializers.Serializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=models.Ingredient.objects.all()
    )

    def create(self, validated_data):
        return models.Recipe.objects.create(user=self.context['user'])


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = account_models.User
        fields = ("telegram_id", "username",)
