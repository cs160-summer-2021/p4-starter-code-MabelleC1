# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('layouts/', views.layouts, name='layouts'),
    path('layouts/layout1/', views.layout1, name='layout1'),
    path('layouts/layout2/', views.layout2, name='layout2'),
    path('small/', views.small, name='small'),
    # path('<str:room_name>/', views.room, name='room'),

]
