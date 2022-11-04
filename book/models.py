from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg

from author.models import Author, Genre


class Book(models.Model):
    title = models.CharField('Название книги', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    genre = models.ForeignKey(
        Genre,
        verbose_name='Жанр',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.DO_NOTHING,
        verbose_name='Автор'
    )
    description = models.TextField('Описание книги')
    publication_date = models.DateField('Дата публикации')

    def average_rating(self) -> float:
        rating = Review.objects.filter(book=self).aggregate(Avg("rating"))["rating__avg"] or 0
        return rating

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='review',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    rating = models.IntegerField(default=0)
    text = models.TextField('Описание')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Последнее измененин', auto_now=True)
    active = models.BooleanField('Активный комментарий', default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.user} on {self.book}'


class BookMark(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='bookmark',
    )

    def __str__(self):
        return self.user.username
