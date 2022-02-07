
from django.urls import path
from . import views

urlpatterns = [
    path('<str:gpname>/',views.index,name='index'),
]