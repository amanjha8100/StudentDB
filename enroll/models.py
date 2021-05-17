from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    roll = models.IntegerField(default=0)

    class Meta:
        ordering = ['roll']

    def __str__(self):
        return self.name