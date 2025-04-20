from django.contrib import admin
from .models import Category, Books, Connection

admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Connection)