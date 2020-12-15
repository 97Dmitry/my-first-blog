from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    """ Модель постов """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заглавие',
                             validators=[validators.RegexValidator(regex=r'[@#$%&*]+',
                                                                   message='Заголовок должен состоять из букв и цифр',
                                                                   inverse_match=True),
                                         validators.MinLengthValidator(5, message='Длина заголовка меньше 5 символов')])
    text = models.TextField(verbose_name='Текст',
                            validators=[validators.MinLengthValidator(120, message='Длина текста меньше 150 символов')])
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.SET_NULL, verbose_name='Тег')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title  # Из БД будет возвращаться тайтл экземпляра в виде строки

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        ordering = ['-created_date', ]


class Rubric(models.Model):
    """ Модель рубрик для постов """
    rubric = models.CharField(max_length=25, db_index=True, verbose_name='Тег')

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'
        ordering = ['rubric']

    def __str__(self):  # Указывает на то, что все теги
        return self.rubric  # будут называется своим именем


class Comments(models.Model):
    """ Комментарии к постам """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Комментатор')
    email = models.EmailField(blank=True, null=True, help_text='Не обязательное полне')
    comment = models.TextField(max_length=1000, verbose_name='Комментарий',
                               help_text='Комментарий может содержать от 15 до 1000 символов',
                               validators=[validators.MinLengthValidator(15,
                                                                         message='Длина текста меньше 15 символов')])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарии'
        ordering = ('created',)

    def __str__(self):
        return f'Комментарий {self.name} к посту {self.post}'

# class Rating(models.Model):
#     """ Числовые значения рейтинга """
#     value = models.SmallIntegerField(verbose_name='Оценка', default=0)
#
#     def __str__(self):
#         return f'{self.value}'
#
#     class Meta:
#         verbose_name = 'Оценка'
#         verbose_name_plural = 'Оценки'
#         ordering = ['-value']
#
#
# class ValueRatingPost(models.Model):
#     """ Модель оценки постов """
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
#     rating = models.ForeignKey(Rating, on_delete=models.CASCADE, verbose_name='Оценка')
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Запись', )
#
#     class Meta:
#         verbose_name = 'Рейтинг'
#         verbose_name_plural = 'Рейтинги'
#         ordering = ['post']
#
#     def sum_values_post(pk):
#         a = ValueRatingPost.objects.get(post_id=pk)
#         b = a.values('rating').aggregate(Sum('rating'))
#
#     def __str__(self):
#         return f'{self.rating} - {self.post}'
