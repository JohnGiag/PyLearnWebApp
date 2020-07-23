from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from codingExercise.models import Chapter



class Example(models.Model):
    """
    The Example model is used to create an object that models a coding example.
    It has 4 fields, chapter (the Chapter it belongs to), order (a field used show the order in witch an example should
    be read), title, content.
    """
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    order = models.IntegerField(blank=True, null=True, default=0)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
