from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='def.jpg', upload_to='user_pic')
    user_rank = models.ManyToManyField('Rank', verbose_name='Ранг')

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'

    def __str__(self):
        return f'{self.user.username}'


class Rank(models.Model):
    rank = models.CharField(max_length=25, verbose_name='Ранг')

    class Meta:
        verbose_name_plural = 'Ранги'
        verbose_name = 'Ранг'
        ordering = ['rank']

    def __str__(self):
        return self.rank
