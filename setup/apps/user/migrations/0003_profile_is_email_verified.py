# Generated by Django 3.2 on 2022-06-17 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220613_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_email_verified',
            field=models.BooleanField(default=False, verbose_name='Email Verified'),
        ),
    ]
