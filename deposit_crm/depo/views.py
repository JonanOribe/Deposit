from django.shortcuts import render
from rest_framework import generics,serializers
from .models import Deposit,Article
from .serializers import DepositSerializer,ArticleSerializer
# Create your views here.

class DepositToList(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

class DepositDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

class ArticleToList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
