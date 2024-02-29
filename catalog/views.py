from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

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
        'num_pertcular_books': num_pertcular_books,
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.filter(title__icontains='dream')[:5]  # get 4 book containing dream

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.all()  # get 4 book containing dream

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'

    # def get_queryset(self):
    #     return Author.objects.all()

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get the context
    #     context = super(AuthorDetailView, self).get_context_data(**kwargs)
    #     # Create any data and add it to the context
    #     context={
    #         'Book_details' : Book.objects.all().filter(author_id=self.model.id)
    #     }
    #     return context
    