from django.db import models
from django.conf import settings

# Create your models here.

class Author(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    real_firstname = models.CharField(max_length=25)
    real_lastname = models.CharField(max_length=25)

    def __str__(self):
        return self.author

