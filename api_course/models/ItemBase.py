from django.db import models
from django.utils import timezone


class ItemBase(models.Model):
    subject = models.CharField(max_length=25, null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.subject


