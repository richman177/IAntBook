from rest_framework import viewsets
from .serializers import CategorySerializers, BooksSerializers, ConnectionSerializers
from .models import Category, Books, Connection


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class BooksViewSets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers


class ConnectionViewSets(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializers
