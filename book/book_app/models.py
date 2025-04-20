from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=64, verbose_name='Бөлүм')

    def __str__(self):
        return self.category_name


class Books(models.Model):
    book_pdf = models.FileField(upload_to='book_pdf', verbose_name='Китептин PDF фарматы')
    book_name = models.CharField(max_length=64, verbose_name='Китептин аты')
    book_author = models.CharField(max_length=64, verbose_name='Автору')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Бөлүм')
    publication_year = models.CharField(max_length=32, verbose_name='Басылган жылы')
    loading_time = models.DateTimeField(auto_now=True, verbose_name='Жүктөлгөн убакыт')

    def __str__(self):
        return self.book_name


class Connection(models.Model):  #Байланыш
    connection = models.URLField(verbose_name='Байланыш')

    def __str__(self):
        return self.connection



class BookLike(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('book', 'ip_address')

    def __str__(self):
        return f'{self.ip_address} liked {self.book.book_name}'
