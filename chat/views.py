from django.shortcuts import render

# Create your views here.

def chat(request):
    return render(request, 'chat/chat.html')

def room(request, room_name):
    context = {
        'room_name': room_name,

        }
    return render(request, 'chat/room.html', context)
