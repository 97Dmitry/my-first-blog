from django.contrib.auth.models import User
from django.db import models


class BlogUser(models.Model):
    username = None
    email = None
    password1 = None
    password2 = None
