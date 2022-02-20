from  django.http import HttpResponse
from django.shortcuts import render
from . import models,forms
from django.shortcuts import render, get_object_or_404

def book_list(request):
    booksc = models.Book.objects.all()
    return render(request, 'book_list.html', {'booksc': booksc})

def book_detail(request, id):
    books = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'books': books})

def create_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('book created')
    else:
        form = forms.BookForm()
        return render(request, 'add_book.html', {'form':form})