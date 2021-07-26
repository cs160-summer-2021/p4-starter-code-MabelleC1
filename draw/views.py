# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'draw/index.html')

def layouts(request):
    return render(request, 'draw/layouts.html')

def layout1(request):
    return render(request, 'draw/layout1.html')

def layout2(request):
    return render(request, 'draw/layout2.html')

def small(request):
    return render(request, 'draw/small.html')

# def room(request, room_name):
#     return render(request, 'draw/room.html', {
#         'room_name': room_name
#     })
