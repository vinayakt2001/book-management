from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('authors', views.authors, name='authors'),
    path('authors/create_author', views.create_author, name='create_author'),
    path('authors/list_author', views.list_author, name='list_author'),
    path('books', views.books, name='books'),
    path('books/add_book', views.add_book, name='add_book'),
    path('books/list_book', views.list_book, name='list_book'),
    path('ratings', views.ratings, name='ratings'),
    path('ratings/author_rating', views.author_rating, name='author_rating'),
    path('ratings/book_rating', views.book_rating, name='book_rating'),
    path('reviews', views.reviews, name='reviews'),

]