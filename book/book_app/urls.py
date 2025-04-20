from .views import CategoryViewSets, BooksViewSets, ConnectionViewSets
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'category', CategoryViewSets, basename='category'),
router.register(r'books', BooksViewSets, basename='books'),
router.register(r'connection', ConnectionViewSets, basename='connection'),

urlpatterns = [
    path('', include(router.urls)),
]