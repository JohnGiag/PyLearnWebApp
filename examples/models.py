from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from codingExercise.models import Chapter


# Create your models here.


class Example(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    order = models.IntegerField(blank=True, null=True, default=0)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
