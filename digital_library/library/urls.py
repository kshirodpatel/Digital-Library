from django.urls import path
from . import views

urlpatterns = [
    path( '', views.home, name='home-page' ),
    path( 'books/', views.browseBooks, name='books' ),
    path( 'book-details', views.bookDetails, name='book-details' )
]