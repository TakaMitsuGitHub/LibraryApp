from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BookSerializer
from .models import Book, Library
from .process.create_csv import CreateBook


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


@api_view(['GET', 'POST'])
def create_book_csv(request):
    create_book = CreateBook(2)
    create_book.create_csv()
    return Response({"message": "create_csv OK"})




    # from rest_framework.views import APIView
    # from rest_framework.response import Response
    # from rest_framework import status
    # from .models import Book
    # from .serializers import BookSerializer
    #
    # class BookDetailView(APIView):
    #     def get(self, request, isbn):
    #         try:
    #             book = Book.objects.get(isbn=isbn)
    #             serializer = BookSerializer(book)
    #             return Response(serializer.data)
    #         except Book.DoesNotExist:
    #             return Response(
    #                 {"error": "指定されたISBNの書籍は存在しません。"},
    #                 status=status.HTTP_404_NOT_FOUND)
