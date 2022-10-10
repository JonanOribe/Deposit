from xml.parsers.expat import model
from django.db import models

# Create your models here.
COLORS = (
    ('0','White'),
    ('1','Black'),
    ('2','Red'),
    ('3','Blue'),
    ('4','Yellow'),
)
class Deposit(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=30)

class Article(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=30)
    quantity = models.IntegerField()
    color = models.CharField(max_length = 1, choices=COLORS)
    deposit = models.ForeignKey(Deposit,null=True, on_delete=models.SET_NULL)

