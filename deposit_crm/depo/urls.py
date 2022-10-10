from django.urls import path
from django.urls import re_path as url

from . import views

urlpatterns = [
    url(r'^deposit$', views.DepositToList.as_view()),
    url(r'^deposit/(?P<pk>[0-9]+)$', views.DepositDetail.as_view()),
    url(r'^article$', views.ArticleToList.as_view()),
    url(r'^article/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),
]
