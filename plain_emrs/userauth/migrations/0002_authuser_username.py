# Generated by Django 4.2.6 on 2023-12-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authuser',
            name='username',
            field=models.CharField(default='default_user', max_length=75),
        ),
    ]