from rest_framework import viewsets, generics
from .models import Category, Books, Connection, BookLike
from .serializers import (CategorySerializer, BooksDetailSerializer, ConnectionSerializer, BookLikeSerializer,
                          BooksListSerializer)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BooksListAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksListSerializer


class BooksDetailAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksDetailSerializer


class ConnectionListAPIView(generics.ListAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class BookLikeViewSet(viewsets.ModelViewSet):
    queryset = BookLike.objects.all()
    serializer_class = BookLikeSerializer
