from django.shortcuts import render
from .models import Book

# Create your views here.

def book_listview(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
