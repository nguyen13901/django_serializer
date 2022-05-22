from django.db import models
from django.utils import timezone
from api_course.models import Category, ItemBase


class Course(ItemBase):
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "course"
        unique_together = ('subject', 'category')

