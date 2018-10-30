from rest_framework.serializers import ModelSerializer
from . import models


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class NewsSerializer(ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'
