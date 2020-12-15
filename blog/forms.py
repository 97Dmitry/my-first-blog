from django import forms
from .models import Post, Comments, ValueRatingPost

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'rubric', 'text')

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment', 'email')


class RatingForm(forms.ModelForm):

    class Meta:
        model = ValueRatingPost
        fields = ('rating', 'post')