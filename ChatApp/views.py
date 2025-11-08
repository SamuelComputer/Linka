from django.shortcuts import render, redirect
from .models import Room, Message
from django.utils import timezone

# Create or join a room
def CreateRoom(request):
    if request.method == 'POST':
        room_name = request.POST.get('room')
        username = request.POST.get('username')
        
        # Get or create the room
        room, created = Room.objects.get_or_create(room_name=room_name)
        
        return redirect('room', room_name=room_name, username=username)

    return render(request, 'index.html')


# View messages in a room
def MessageView(request, room_name, username):
    room = Room.objects.get(room_name=room_name)
    messages = Message.objects.filter(room=room).order_by('date')

    if request.method == 'POST':
        message_text = request.POST.get('message', '').strip()

        if message_text:  # only save non-empty messages
            Message.objects.create(
                room=room,
                sender=username,
                message=message_text,
                date=timezone.now()
            )

        return redirect('room', room_name=room_name, username=username)

    # Get all rooms for the user (for sidebar)
    all_rooms = Room.objects.all()  # for now, just show all rooms

    context = {
        'room_name': room_name,
        'username': username,
        'messages': messages,
        'all_rooms': all_rooms,  # pass to template
    }
    return render(request, '_message.html', context)
