from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='user_pic\\def.jpg', upload_to='user_pic')

    def __str__(self):
        return f'{self.user.username}'
