from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core import validators

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заглавие',
                             validators=[validators.RegexValidator(regex=r'\W+',
                                                                   message='Заголовок должен состоять из букв и цифр',
                                                                   inverse_match=True)])
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Тег')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title # Из БД будет возвращаться тайтл экземпляра в виде строки


class Rubric(models.Model):

    rubric = models.CharField(max_length= 25, db_index=True, verbose_name='Тег')

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'
        ordering = ['rubric']

    def __str__(self):      # Указывает на то, что все теги
        return self.rubric  # будут называется своим именем