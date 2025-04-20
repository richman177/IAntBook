from rest_framework import serializers
from .models import Category, Books, Connection



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class BooksSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    loading_time = serializers.DateTimeField(format('%d-%m-%Y'))

    class Meta:
        model = Books
        fields = '__all__'


class ConnectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'