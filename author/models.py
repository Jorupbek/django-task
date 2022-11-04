from django.db import models


class Author(models.Model):
    name = models.CharField('Автор', max_length=255)
    slug = models.SlugField('Слаг', unique=True)
    date_of_birth = models.DateField('Дата рождения')
    date_of_death = models.DateField('Дата смерти')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=32, unique=True)
    slug = models.SlugField('Слаг', unique=True)

    def __str__(self):
        return self.name
