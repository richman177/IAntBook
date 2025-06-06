from rest_framework import serializers
from .models import Category, Books, Connection, BookLike, BookViewing


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class BookLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLike
        fields = ['id', 'book', 'unique_field', 'liked_at']


class BookViewingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookViewing
        fields = ['id', 'book_viewing', 'unique']


class BooksListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Books
        fields = ['id', 'book_name', 'book_image', 'book_author', 'publication_year', 'category']


class BooksDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    loading_time = serializers.DateTimeField(format='%d-%m-%Y', read_only=True)
    like_count = serializers.SerializerMethodField()
    viewing_count = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = ['id', 'book_pdf', 'book_name', 'book_image', 'book_author', 'category',
                  'publication_year', 'loading_time', 'description', 'like_count', 'viewing_count']

    def get_like_count(self, obj):
        return obj.get_like_count()

    def get_viewing_count(self, obj):
        return obj.get_viewing_count()


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'
