# Generated by Django 4.1.3 on 2022-11-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Автор')),
                ('slug', models.SlugField(unique=True, verbose_name='Слаг')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('date_of_death', models.DateField(verbose_name='Дата смерти')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Жанр')),
            ],
        ),
    ]
