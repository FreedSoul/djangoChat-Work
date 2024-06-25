from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = models.Manager()
    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=100)
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room = models.CharField(max_length=1000, default="Default")

    # def __str__(self):
    #     return self.name