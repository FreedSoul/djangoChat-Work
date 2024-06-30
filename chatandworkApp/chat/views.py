from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from chat.models import Room
from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'home.html')

def chat_rooms(request):
    allrooms = Room.objects.all()    
    context = {
        'rooms': allrooms
    }
    return render(request, 'chatrooms.html', context)

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def room(request, room):
    #if the keyvalue is not secure must use request.GET.get('key','mydefaultincasedoesntexist')
    user = request.GET.get('username','')
    get_object_or_404(Room, name=room)
    context = {
        'user': user,
        'room': room
    }
    # print("esto es getroom",getroom)
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

def sendmessage(request):
    message = request.POST['message']
    room = request.POST['room']
    # username = request.POST['username']

    # print(message, room, username)
    return HttpResponse('Message sent successfully')