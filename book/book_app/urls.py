from django.urls import path, include
from rest_framework import routers
from .views import CategoryListAPIView, BooksListAPIView, ConnectionListAPIView, BookLikeViewSet, BooksDetailAPIView

router = routers.SimpleRouter()
router.register(r'likes', BookLikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BooksListAPIView.as_view(), name='book_list'),
    path('books/<int:pk>/', BooksDetailAPIView.as_view(), name='books_detail'),
    path('category', CategoryListAPIView.as_view(), name='category'),
    path('connection', ConnectionListAPIView.as_view(), name='connection')
]
