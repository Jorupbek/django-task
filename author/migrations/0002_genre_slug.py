# Generated by Django 4.1.3 on 2022-11-03 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='Слаг'),
            preserve_default=False,
        ),
    ]