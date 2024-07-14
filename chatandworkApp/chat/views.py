from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from chat.models import Room, Message
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
    room_details = Room.objects.get(name=room)
    context = {
        'user': user,
        'room': room,
        'room_details': room_details
    }
    # print("esto es getroom",getroom)
    return render(request, 'room.html', context)

def newroom(request):
    return render(request, 'newroom.html')

def register_room(request):
    template = loader.get_template('room.html')
    #agregar admin(username) en el room.model, y no enviar username atraves de url 
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
    room = request.POST['room_id']
    username = request.POST['username']

    print("pruebaaa",message, room, username)
    new_message = Message.objects.create(text=message, room=room, user=username)
    new_message.save()
    return redirect('/')
    # return HttpResponse('Message sent successfully')

def getmessages(request, room):
    room_details = Room.objects.get(name=room)
    print('estos son los detalletes',room_details.pk)
    messages = Message.objects.filter(room=room_details.pk)
    print(messages.values())
    return JsonResponse({"messages": list(messages.values())})