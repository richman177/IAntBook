from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Books, Connection, BookLike, BookViewing
from .serializers import (CategorySerializer, BooksDetailSerializer, ConnectionSerializer, BookLikeSerializer,
                          BooksListSerializer, BookViewingSerializer)
from django.http import FileResponse, Http404


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BooksListAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksListSerializer


class BooksDetailAPIView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksDetailSerializer


class ConnectionListAPIView(generics.ListAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer


class BookLikeViewSet(generics.CreateAPIView):
    queryset = BookLike.objects.all()
    serializer_class = BookLikeSerializer


class BookViewingViewSet(generics.CreateAPIView):
    queryset = BookViewing.objects.all()
    serializer_class = BookViewingSerializer



class TopViewedBooksAPIView(APIView):
    def get(self, request):
        all_books = Books.objects.all()
        books_with_views = [(book, book.get_viewing_count()) for book in all_books]
        books_with_views.sort(key=lambda x: x[1], reverse=True)
        top_20_books = books_with_views[:20]

        data = []
        for book, view_count in top_20_books:
            data.append({
                'id': book.id,
                'name': book.book_name,
                'author': book.book_author,
                'view_count': view_count,
                'book_image': book.book_image.url if book.book_image else None,
            })
        return Response(data)



class BookDownloadAPIView(APIView):
    def get(self, request, pk):
        try:
            book = Books.objects.get(pk=pk)
            file_handle = book.book_pdf.open()

            response = FileResponse(file_handle, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{book.book_pdf.name.split("/")[-1]}"'
            return response

        except Books.DoesNotExist:
            raise Http404("Китеп табылган жок.")
