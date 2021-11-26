from django.conf.urls import url

from . import views

app_name = 'ctbuybacks'

urlpatterns = [
    url(r'^$', views.buyback_list, name='list'),
    ]
