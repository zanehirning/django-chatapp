from django.shortcuts import render
from .models import Room, Message
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return render(request, 'chat/home.html')

def room(request, room):
    return render(request, 'chat/room.html')

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)