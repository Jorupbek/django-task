from rest_framework import serializers

from author.serializers import GenreSerializer, AuthorSerializer, UserSerializer
from book.models import Book, Review


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = ('id', 'user', 'rating', 'text',)


class BooksListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    id = serializers.HyperlinkedIdentityField(view_name="book-detail")
    author = AuthorSerializer()
    avg_rating = serializers.CharField(source='average_rating')

    class Meta:
        model = Book
        fields = ("id", "title", "genre", "author", "avg_rating", "slug",)


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()
    author = AuthorSerializer()
    review = ReviewSerializer(many=True)

    class Meta:
        model = Book
        fields = ("id", "title", "genre", "author", "description", "review", "publication_date", "slug",)
