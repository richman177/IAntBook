from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True, verbose_name='Бөлүм')

    def __str__(self):
        return self.category_name


class Books(models.Model):
    book_pdf = models.FileField(upload_to='book_pdf', verbose_name='Китептин PDF фарматы', max_length=1024)
    book_name = models.CharField(max_length=64, verbose_name='Китептин аты')
    book_image = models.ImageField(upload_to='book_images', null=True, blank=True, verbose_name='Китептин суроту')
    book_author = models.CharField(max_length=64, verbose_name='Автору')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Бөлүм')
    publication_year = models.IntegerField(verbose_name='Басылган жылы')
    loading_time = models.DateTimeField(auto_now=True, verbose_name='Жүктөлгөн убакыт')
    description = models.TextField()

    def get_like_count(self):
        # return self.likes.all()
        book_like = self.likes.all()
        if book_like.exists():
            return book_like.count()
        return 0

    def __str__(self):
        return self.book_name


class Connection(models.Model):  #Байланыш
    connection = models.URLField(verbose_name='Байланыш')

    def __str__(self):
        return self.connection



class BookLike(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)
    liked_at = models.DateTimeField(auto_now_add=True)
    unique_field = models.CharField(max_length=50, unique=True)

    class Meta:
        unique_together = ('unique_field', 'book')

    def __str__(self):
        return f'{self.unique_field} liked {self.book.book_name}'
