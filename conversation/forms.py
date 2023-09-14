from django.forms import ModelForm
from .models import ConversationMessage

class ConversationMessageForm(ModelForm):
  class Meta:
    model = ConversationMessage
    fields = ('content',)