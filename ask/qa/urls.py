from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from qa.views import view1, view2, view3

urlpatterns = [ url(r'^$', view1),
                url(r'^popular/', view2),
                url(r'^question/(?P<id>\d+)/$', view3),
 ]
