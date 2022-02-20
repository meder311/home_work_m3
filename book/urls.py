from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list, name='books'),
    path('book_list/<int:id>/', views.book_detail, name='booksdetail'),
]


