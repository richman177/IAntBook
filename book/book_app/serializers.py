from rest_framework import serializers
from .models import Category, Books, Connection


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class BooksSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    loading_time = serializers.DateTimeField(format='%d-%m-%Y')
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = ['id', 'book_name', 'category', 'likes_count', 'loading_time']

    def get_likes_count(self, obj):
        return obj.likes.count()


class BookSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = ['id', 'book_name', 'book_author', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()


class ConnectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'
