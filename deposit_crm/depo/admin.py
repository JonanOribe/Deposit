from django.contrib import admin
from depo.models import Article,Deposit
# Register your models here.

admin.site.register([Deposit,Article])