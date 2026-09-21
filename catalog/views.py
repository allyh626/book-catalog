from django.views.generic import ListView

from .models import Publisher, Book, Review

class BookView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"


class PublisherView(ListView):
    model = Publisher
    template_name = "publisher_list.html"
    context_object_name = "publishers"


class ReviewView(ListView):
    model = Review
    template_name = "review_list.html"
    context_object_name = "reviews"


