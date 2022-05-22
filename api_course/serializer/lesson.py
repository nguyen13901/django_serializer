from rest_framework import serializers
from api_course.models import Lesson
from api_course.serializer import TagSerializer


class LessonSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ["id", "subject", "content", "created_at", "course", "tags"]

