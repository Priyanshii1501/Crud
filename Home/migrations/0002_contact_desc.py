# Generated by Django 5.0.1 on 2024-01-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='Some default value', max_length=255),
        ),
    ]