# Generated by Django 3.2.7 on 2021-09-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='anonymous',
            field=models.BooleanField(default=False),
        ),
    ]
