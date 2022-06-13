from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

rooms = [
    { 'id': 1, 'name': 'Room 1', 'description': 'This is room 1' },
    { 'id': 2, 'name': 'Room 2', 'description': 'This is room 2' },
    { 'id': 3, 'name': 'Room 3', 'description': 'This is room 3' },
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
            break
    context = {'room': room}
    return render(request, 'base/room.html', context)