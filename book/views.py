from rest_framework import viewsets

from book.models import Book, Review
from book.serializers import BookSerializer, BooksListSerializer, ReviewSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        serializer_map = {
            'retrieve': BookSerializer,
            'list': BooksListSerializer
        }

        return serializer_map.get(self.action, BookSerializer)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# todo Осталось реализовать избранное в DRF и вывести его
# todo Осталось реализовать оставлять комментарий и рейтинг
