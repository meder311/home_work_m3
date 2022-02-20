from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_list, name='books'),
]