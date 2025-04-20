from rest_framework import viewsets
from .serializers import CategorySerializers, BooksSerializers, ConnectionSerializers
from .models import Category, Books, Connection, BookLike
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Books



class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class BooksViewSets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers


class ConnectionViewSets(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializers


class BookLikeAPIView(APIView):
    def post(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        ip_address = request.META.get('REMOTE_ADDR')

        if not BookLike.objects.filter(book=book, ip_address=ip_address).exists():
            BookLike.objects.create(book=book, ip_address=ip_address)
            return Response({"message": "Лайк ийгиликтүү кошулду!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Сиз бул китепке мурда лайк койгонсуз."}, status=status.HTTP_400_BAD_REQUEST)


class BookDetailAPIView(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        likes_count = book.likes.count()

        data = {
            "id": book.id,
            "title": book.title,
            "likes_count": likes_count,
        }
        return Response(data)


class BookDetailAPIView(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        serializer = BooksSerializers(book)
        return Response(serializer.data)