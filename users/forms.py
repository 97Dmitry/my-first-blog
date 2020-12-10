from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Profile


class SingUp(UserCreationForm):
    username = forms.CharField(help_text='Имя аккаунта может содержать только буквы, цифры и знаки подчеркивания',
                               validators=[validators.RegexValidator(
                                   regex=r'[@#$%&*]+', message='Заголовок должен состоять из букв и цифр',
                                   inverse_match=True), validators.MinLengthValidator(
                                   3, message='Длина имени меньше 3 символов'),
                                   validators.MaxLengthValidator(25, message='Длина имени больше 25 символов')])

    password1 = forms.CharField(help_text='Пароль должен состоять из букв и цифр',
                                validators=[validators.RegexValidator(
                                    regex=r'[@#$%&*]+', message='Заголовок должен состоять из букв и цифр',
                                    inverse_match=True), validators.MinLengthValidator(
                                    8, message='Длина пароля меньше 8 символов')],
                                widget=forms.PasswordInput())  # Параметр widget определяет как будет себя вести форма

    password2 = forms.CharField(help_text='Пароль должен состоять из букв и цифр',
                                validators=[validators.RegexValidator(
                                    regex=r'[@#$%&*]+', message='Заголовок должен состоять из букв и цифр',
                                    inverse_match=True), validators.MinLengthValidator(
                                    8, message='Длина пароля меньше 8 символов')],
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ChangePassword(PasswordChangeForm):
    new_password1 = forms.CharField(help_text='Пароль должен состоять из букв и цифр',
                                    validators=[validators.RegexValidator(
                                        regex=r'[@#$%&*]+', message='Заголовок должен состоять из букв и цифр',
                                        inverse_match=True), validators.MinLengthValidator(
                                        8, message='Длина пароля меньше 8 символов')],
                                    widget=forms.PasswordInput())
    new_password2 = forms.CharField(help_text='Пароль должен состоять из букв и цифр',
                                    validators=[validators.RegexValidator(
                                        regex=r'[@#$%&*]+', message='Заголовок должен состоять из букв и цифр',
                                        inverse_match=True), validators.MinLengthValidator(
                                        8, message='Длина пароля меньше 8 символов')],
                                    widget=forms.PasswordInput())

    class Meta:
        model = User


class ChangeUserDataForm(forms.ModelForm):
    username = forms.CharField(help_text='Имя аккаунта может содержать только буквы, цифры и знаки подчеркивания',
                               validators=[validators.RegexValidator(
                                   regex=r'[@#$%&*]+', message='Заголовок должен состоять из букв и цифр',
                                   inverse_match=True), validators.MinLengthValidator(
                                   3, message='Длина имени меньше 3 символов'),
                                   validators.MaxLengthValidator(25, message='Длина имени больше 25 символов')])

    class Meta:
        model = User
        fields = ('username', 'email')


class UserAvatarPicture(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserAvatarPicture, self).__init__(*args, **kwargs)
        self.fields['picture'].label = 'Изображение профиля '

    class Meta:
        model = Profile
        fields = ('picture',)


class RecoveryPassword(SetPasswordForm):
    new_password1 = forms.CharField(label='Новый пароль',
                                    help_text='Пароль должен состоять из букв и цифр',
                                    validators=[validators.RegexValidator(
                                        regex=r'[@#$%&*]+', message='Пароль должен состоять из букв и цифр',
                                        inverse_match=True), validators.MinLengthValidator(
                                        8, message='Длина пароля меньше 8 символов')],
                                    widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Повторите новый пароль',
                                    help_text='Пароль должен состоять из букв и цифр',
                                    validators=[validators.RegexValidator(
                                        regex=r'[@#$%&*]+', message='Пароль должен состоять из букв и цифр',
                                        inverse_match=True), validators.MinLengthValidator(
                                        8, message='Длина пароля меньше 8 символов')],
                                    widget=forms.PasswordInput())
