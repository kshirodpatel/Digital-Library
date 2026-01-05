from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def browseBooks(request):
    context = {}
    return render(request, 'books.html', context)

def bookDetails(request):
    context = {}
    return render(request, 'book-details.html', context)
