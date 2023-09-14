from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm

# Create your views here.

@login_required
def new_conversation(request, item_id):
  item = get_object_or_404(Item, id=item_id)

  if item.created_by == request.user:
    return redirect("conversation:index")
  
  existing_conversation = Conversation.objects.filter(item=item, participants__in=[request.user.id])
  if existing_conversation:
    return redirect("conversation:detail", convers_id=existing_conversation[0].id)

  if request.method == "POST":
    form = ConversationMessageForm(data=request.POST)
    if form.is_valid():
      conversation = Conversation.objects.create(item=item)
      conversation.participants.add(request.user)
      conversation.participants.add(item.created_by)
      conversation.save()

      conversation_message = form.save(commit=False)
      conversation_message.conversation = conversation
      conversation_message.created_by = request.user
      conversation_message.save()

      return redirect("conversation:detail", convers_id=conversation.id)
  else:
    form = ConversationMessageForm()
  
  context = {"form": form, "item": item}
  return render(request, "conversation/new.html", context)

@login_required
def inbox(request):
  converstaions = Conversation.objects.filter(participants__in=[request.user.id])
  context = {"conversations": converstaions}
  return render(request, "conversation/inbox.html", context)

@login_required
def detail(request, convers_id):
  conversation = get_object_or_404(Conversation, id=convers_id, participants__in=[request.user.id])
  if request.method == "POST":
    form = ConversationMessageForm(data=request.POST)
    if form.is_valid():
      conversation_message = form.save(commit=False)
      conversation_message.created_by = request.user
      conversation_message.conversation = conversation
      conversation_message.save()

      conversation.save()

      form = ConversationMessageForm()
  else:
    form = ConversationMessageForm()
  context = {"conversation": conversation, "form": form}

  return render(request, "conversation/detail.html", context)

