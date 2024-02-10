from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from  .models import Book


class Index(TemplateView):
    template_name = 'index.html'



class BookDetailView(APIView):
    def get(self, request, isbn):
        try:
            book = Book.objects.get(isbn=isbn)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response(
                {"error": "指定されたISBNの書籍は存在しません。"},
                status=status.HTTP_404_NOT_FOUND)
