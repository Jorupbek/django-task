from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'authors-list': reverse('authors-list', request=request, format=format),
        'books-list': reverse('books-list', request=request, format=format),
        'genre-list': reverse('genre-list', request=request, format=format),
    })
