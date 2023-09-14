from django.db import models
from django.contrib.auth.models import User
from item.models import Item

# Create your models here.
class Conversation(models.Model):

  item = models.ForeignKey(Item, related_name="conversations", on_delete=models.CASCADE)
  participants = models.ManyToManyField(User, related_name="conversations")
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('-modified',)

class ConversationMessage(models.Model):
  conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
  content = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, related_name="user_messages", on_delete=models.CASCADE)
