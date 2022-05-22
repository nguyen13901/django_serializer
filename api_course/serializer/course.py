from rest_framework import serializers
from api_course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "subject", "image", "created_at", "category"]

