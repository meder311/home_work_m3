
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class BookComment(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books_comment')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.books.title