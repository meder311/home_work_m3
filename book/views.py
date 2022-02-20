from django.shortcuts import render
from . import models

def book_list(request):
    booksc = models.Book.objects.all()
    return render(request, 'book_list.html', {'booksc': booksc})

