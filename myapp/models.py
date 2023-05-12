from django.db import models

# Create your models here.

class Example(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField()

    def __str__(self):
        return self.name
