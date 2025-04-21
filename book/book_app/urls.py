from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BooksViewSet, ConnectionViewSet, BookLikeAPIView, BookDetailAPIView

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'books', BooksViewSet, basename='books')
router.register(r'connection', ConnectionViewSet, basename='connection')

urlpatterns = [
    path('', include(router.urls)),
    path('books/<int:book_id>/like/', BookLikeAPIView.as_view(), name='book-like'),
    path('books/<int:book_id>/', BookDetailAPIView.as_view(), name='book-detail'),
]