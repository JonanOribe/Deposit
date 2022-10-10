from django.shortcuts import render
from rest_framework import generics,serializers
from .models import Deposit,Article
from .serializers import DepositSerializer,ArticleSerializer
# Create your views here.

class DepositToList(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializers_class = DepositSerializer(queryset, many=True)

class DepositDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposit.objects.all()
    serializers_class = DepositSerializer(queryset, many=True)

class ArticleToList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializers_class = ArticleSerializer(queryset, many=True)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializers_class = ArticleSerializer(queryset, many=True)
