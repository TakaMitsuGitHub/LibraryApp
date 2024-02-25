from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from  .models import Book

import pandas as pd

import csv




class Index(TemplateView):
    template_name = 'index.html'



# api
# CSVからデータをインポートする関数
@api_view(["post"])
def import_books_from_csv(request):

    print(request)

    file_path = "./Book1.csv"
    df = pd.read_csv(file_path)
    for idx, row in df.iterrows():
        book = Book.from_csv_row(row)
        book.save()

    # with open(csv_file, mode='r', encoding='utf-8') as file:
    #     reader = csv.DictReader(file)
    #
    #     for row in reader:
    #         book = Book.from_csv_row(row)
    #         book.save()

    return Response({"messages": "OK"})


