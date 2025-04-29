from django.urls import path
from .views import TopViewedBooksAPIView
from .views import (CategoryListAPIView, BooksListAPIView, ConnectionListAPIView,
                    BookLikeViewSet, BooksDetailAPIView, BookViewingViewSet, BookPDFListAPIView)



urlpatterns = [
    path('books/', BooksListAPIView.as_view(), name='book_list'),
    path('books/<int:pk>/', BooksDetailAPIView.as_view(), name='books_detail'),
    path('category/', CategoryListAPIView.as_view(), name='category'),
    path('connection/', ConnectionListAPIView.as_view(), name='connection'),
    path('like/', BookLikeViewSet.as_view(), name='like'),
    path('viewing/', BookViewingViewSet.as_view(), name='viewing'),
    path('top-books/', TopViewedBooksAPIView.as_view(), name='top_books'),
    path('pdf/', BookPDFListAPIView.as_view(), name='book_pdf'),
]
