# Generated by Django 4.2.6 on 2023-11-03 23:01

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email_address',
            field=models.EmailField(blank=True, default='No email', max_length=254),
        ),
    ]
