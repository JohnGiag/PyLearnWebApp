from django.db import models


# Create your models here.

class Chapter(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Exercise(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, default=0)
    name = models.CharField(max_length=100, null=False, blank=False, )
    instructions = models.TextField(null=False, blank=False)
    test_imports = models.TextField(blank=True)
    test = models.TextField(null=False, blank=False)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
