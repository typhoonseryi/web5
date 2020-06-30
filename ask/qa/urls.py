from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from qa.views import test

urlpatterns = [ url(r'^', test) ]
