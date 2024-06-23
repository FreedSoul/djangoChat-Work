from django.http import HttpResponse
from django.shortcuts import render, redirect
from chat.models import Room
from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'home.html')

def chat_rooms(request):
    return render(request, 'chatrooms.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def room(request, room):
    user = request.GET['username']
    context = {
        'user': user,
        'room': room
    }
    return render(request, 'room.html', context)

def newroom(request):
    return render(request, 'newroom.html')

def register_room(request):
    template = loader.get_template('room.html')
    room = request.POST['room_name']
    user = request.POST['username']
    
    # return HttpResponse(template.render(context, request))
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+user)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+user)
