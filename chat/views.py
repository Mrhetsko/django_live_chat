from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html')


def chat():
    pass


def room(request, room_name: str):
    return render(request, 'chat/chatroom.html', {
        'room_name': room_name
    })
