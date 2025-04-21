from rest_framework import serializers
from .models import Category, Books, Connection


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']  # id талаасын коштук


class BooksSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Категория маалыматы окуу үчүн гана
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)  # Жазуу үчүн
    loading_time = serializers.DateTimeField(format='%d-%m-%Y', read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = [
            'id', 'book_pdf', 'book_name', 'book_image', 'book_author',
            'category', 'category_id', 'publication_year', 'loading_time',
            'description', 'likes_count'
        ]

    def get_likes_count(self, obj):
        return obj.likes.count()


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = ['id', 'connection']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = ['id', 'book_name', 'book_author', 'category', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()