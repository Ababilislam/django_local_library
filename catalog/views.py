from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, BookInstance, Author, Genre


# Create your views here.

def index(request):
    title = 'Local Library Home'
    """view function for home page of site."""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # avabilable book(status =a)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # the all() is implied by default
    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()
    num_pertcular_books = Book.objects.filter(title='the dream').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'title': title,
        'num_genres': num_genres,
        'num_pertcular_books':num_pertcular_books,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
