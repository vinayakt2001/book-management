from django.shortcuts import render, HttpResponse
from django.db.models import Avg
from .models import Author, Book, Review
# Create your views here.


def index(request):
    return render(request, 'index.html')


def authors(request):
    return render(request, 'authors.html')


def create_author(request):
    if request.method == 'POST':
        author_name = request.POST['author_name']
        new_auth = Author(name=author_name)
        new_auth.save()
        return HttpResponse('Author Added Successfully..!!')
    elif request.method == 'GET':
        return render(request, 'create_author.html')
    else:
        return HttpResponse('An Exception Occurred! Author Has Not Been Added')


def list_author(request):
    auths = Author.objects.all()
    for auth in auths:
        book_count = Book.objects.filter(author=auth).count()
        auth.book_count = book_count
    context = {
        'auths': auths
    }
    print(context)
    return render(request, 'list_author.html', context)


def books(request):
    return render(request, 'books.html')


def add_book(request):
    auths = Author.objects.all()
    context = {
        'auths': auths
    }
    print(context)
    if request.method == 'POST':
        book_name = request.POST['book_name']
        author_id = request.POST['auth_id']
        author = Author.objects.get(id=author_id)
        new_book = Book(name=book_name, author=author)
        new_book.save()
        return HttpResponse('Book Added Successfully..!!')
    elif request.method == 'GET':
        return render(request, 'add_book.html', context)
    else:
        return HttpResponse('An Exception Occurred! Book Has Not Been Added')


def list_book(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    print(context)
    return render(request, 'list_book.html', context)


def ratings(request):
    return render(request, 'ratings.html')


def author_rating(request):
    auths = Author.objects.all()
    context = {
        'auths': auths
    }
    print(context)
    if request.method == 'POST':
        author_rating = float(request.POST['author_rating'])
        author_review = request.POST['author_review']
        author_id = request.POST['auth_id']
        author = Author.objects.get(id=author_id)
        author_rv = Review(rating=author_rating, review=author_review, author=author)
        author_rv.save()
        author_rt = Review.objects.filter(author=author).aggregate(Avg('rating'))['rating__avg']
        author.rating = author_rt
        author.save()
        return HttpResponse('Review Added Successfully..!!')
    elif request.method == 'GET':
        return render(request, 'author_rating.html', context)
    else:
        return HttpResponse('An Exception Occurred! Review Has Not Been Added')


def book_rating(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    print(context)
    if request.method == 'POST':
        book_rating = float(request.POST['book_rating'])
        book_review = request.POST['book_review']
        book_id = request.POST['book_id']
        book = Book.objects.get(id=book_id)
        book_rv = Review(rating=book_rating, review=book_review, book=book)
        book_rv.save()
        book_rt = Review.objects.filter(book=book).aggregate(Avg('rating'))['rating__avg']
        book.rating = book_rt
        book.save()
        return HttpResponse('Review Added Successfully..!!')
    elif request.method == 'GET':
        return render(request, 'book_rating.html', context)
    else:
        return HttpResponse('An Exception Occurred! Review Has Not Been Added')


def reviews(request):
    if request.method == 'POST':
        author_id = request.POST['auth_id']
        author = Author.objects.get(id=author_id)
        reviews = Review.objects.filter(author=author)
        context = {
            'reviews': reviews
        }
        print(context)
        return render(request, 'author_review.html', context)
    auths = Author.objects.all()
    context = {
        'auths': auths
    }
    print(context)
    return render(request, 'reviews.html', context)


