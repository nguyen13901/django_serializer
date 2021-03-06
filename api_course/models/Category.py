import uuid

from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, unique=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name