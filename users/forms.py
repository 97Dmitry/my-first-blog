from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile




class SingUp(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ChangePassword(PasswordChangeForm):

    class Meta:
        model = User


class ChangeUserDataForm(forms.ModelForm):

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