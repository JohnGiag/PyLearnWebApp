from django.db import models



class Chapter(models.Model):
    """
    The Chapter model is used to sepperrate our content by theme.
    It has one field name.
    """
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Exercise(models.Model):
    """
    The Exercise model is used to create an object that models a programming exercise.
    It has 6 fields, chapter (the Chapter it belongs to), order (a field used show the order in witch an exercise should
    be completed), name, instructions, test_imports (a textfield to add any libraries needed for the test code to run),
    test ( the test code to verify a submission).
    """
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, default=0)
    name = models.CharField(max_length=100, null=False, blank=False, )
    instructions = models.TextField(null=False, blank=False)
    test_imports = models.TextField(blank=True)
    test = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
