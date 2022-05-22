from django.db import models
from django.utils import timezone
from api_course.models import Course, ItemBase, Tag


class Lesson(ItemBase):
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    class Meta:
        db_table = "lesson"
        unique_together = ('subject', 'course')

