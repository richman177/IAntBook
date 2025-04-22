from django.contrib import admin
from .models import Category, Books, Connection, BookLike

admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Connection)
admin.site.register(BookLike)