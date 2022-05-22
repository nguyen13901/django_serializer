from rest_framework import serializers
from api_course.models import Category


class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = '__all__'
    