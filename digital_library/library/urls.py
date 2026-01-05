from django.urls import path
from . import views

urlpatterns = [
    path( '', views.browseBooks, name='browse-books' ),
    path( 'book-details', views.bookDetails, name='book-details' )
]