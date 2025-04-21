from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category, Books, Connection, BookLike
from .serializers import CategorySerializer, BooksSerializer, ConnectionSerializer, BookSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class BookLikeAPIView(APIView):
    def post(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        ip_address = self.get_client_ip(request)

        if not BookLike.objects.filter(book=book, ip_address=ip_address).exists():
            BookLike.objects.create(book=book, ip_address=ip_address)
            likes_count = book.likes.count()
            return Response(
                {
                    "message": "Лайк ийгиликтүү кошулду!",
                    "likes_count": likes_count
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"message": "Сиз бул китепке мурда лайк койгонсуз."},
            status=status.HTTP_400_BAD_REQUEST
        )

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class BookDetailAPIView(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Books, id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)