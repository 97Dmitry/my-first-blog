# Generated by Django 3.1.3 on 2020-12-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='def.jpg', upload_to='user_pic'),
        ),
    ]