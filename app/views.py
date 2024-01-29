from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Book, Library


class Index(TemplateView):
    template_name = 'index.html'


class LibraryBookList(ListView):
    template_name = 'library_bool_list.html'
    model = Library