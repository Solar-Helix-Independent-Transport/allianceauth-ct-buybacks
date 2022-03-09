from django.urls import re_path

from . import views

app_name = 'ctbuybacks'

urlpatterns = [
    re_path(r'^$', views.buyback_list, name='list'),
    ]
