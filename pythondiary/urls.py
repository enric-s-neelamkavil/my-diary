from django.conf.urls import url
from pythondiary import views
from django.urls import path

urlpatterns = [
    path("",views.home),
]
