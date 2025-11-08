from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=255, unique=True)  # ensure no duplicates
    participants = models.JSONField(default=list, blank=True)  # store usernames

    def __str__(self):
        return self.room_name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField(blank=True)  # only text messages for now
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.message:
            preview = (self.message[:30] + '...') if len(self.message) > 30 else self.message
            return f"{self.sender}: {preview}"
        return f"{self.sender}: (empty)"
