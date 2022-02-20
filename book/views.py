from django.shortcuts import render
from . import models
from django.shortcuts import render, get_object_or_404

def book_list(request):
    booksc = models.Book.objects.all()
    return render(request, 'book_list.html', {'booksc': booksc})

def book_detail(request, id):
    books = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'books': books})
