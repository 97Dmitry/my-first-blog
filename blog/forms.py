from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from .models import Post, Comments, ValueRatingPost


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'rubric', 'text')


class CommentsForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Comments
        fields = ('comment', 'email', 'captcha')


class RatingForm(forms.ModelForm):
    class Meta:
        model = ValueRatingPost
        fields = ('rating',)
