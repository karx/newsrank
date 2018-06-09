from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
# from tutorial.quickstart import views

from . import views 



urlpatterns = [
    path('', views.index, name='index'),
    path('votes', views.VoteList.as_view(), name ='VoteViewSet'),
]