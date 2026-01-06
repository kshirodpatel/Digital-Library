from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.
def home(request):
    books = Book.objects.order_by('?')[:5]
    context = {'books': books}
    return render(request, 'home.html', context)

def browseBooks(request):
    books = Book.objects.all()
    context = {'books' : books}
    return render(request, 'books.html', context)

def bookDetails(request, isbn):
    filteredItem = Book.objects.get(isbn=isbn)
    return render(request, 'book-details.html', {'book': filteredItem})
