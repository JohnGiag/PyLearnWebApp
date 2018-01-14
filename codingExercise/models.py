from django.db import models


# Create your models here.


class Exercise(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, )
    instructions = models.TextField(null=False, blank=False)
    test_imports = models.TextField(blank=True)
    test = models.TextField(null=False, blank=False)
    text = models.TextField(null=True, blank=True)
    next = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.name
