from rest_framework import serializers
from .models import Deposit,Article

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('id','code','description')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','code','description',
        'quantity','color','deposit')