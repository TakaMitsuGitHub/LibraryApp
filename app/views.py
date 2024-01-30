from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book, Library


class Index(TemplateView):
    template_name = 'index.html'


class LibraryBookList(ListView):
    template_name = 'library_bool_list.html'
    model = Library
    context_object_name = "book_list"


# class BookList(ListView):
#     template_name = 'bool_list.html'
#     model = Book
#     context_object_name = "book_list"


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
