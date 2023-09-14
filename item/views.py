from django.shortcuts import render, get_object_or_404, redirect
from django.db.models.query import Q
from django.contrib.auth.decorators import login_required
from .models import Item, Category
from .forms import NewItemForm, EditItemForm
# Create your views here.


def items(request):
  query = request.GET.get("query", "")
  category_id = request.GET.get("category", "")
  if query:
    items = Item.objects.filter(
      Q(name__icontains=query) | 
      Q(description__icontains=query) | 
      Q(created_by__username__icontains=query)
    )
  elif category_id and category_id.isnumeric():
    items = Item.objects.filter(category__id=category_id)
    category_id = int(category_id)
  else:
    items = Item.objects.filter(is_sold=False)
  categories = Category.objects.all()
  context = {"items": items, "query": query, "categories": categories, "category_id": category_id}
  return render(request, 'item/items.html', context)

def detail(request, pk):
  item = get_object_or_404(Item, id=pk)
  current_user_conversation_id = ""
  if request.user.is_authenticated and request.user != item.created_by:
    existing_conversation = item.conversations.filter(participants__in=[request.user])
    if existing_conversation:
      current_user_conversation_id = existing_conversation[0].id

  related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=item.id)[:3]
  context = {"item": item, "related_items": related_items, "current_user_conversation_id": current_user_conversation_id}
  return render(request, 'item/detail.html', context)

@login_required
def new_item(request):
  form_type = "New Item"
  submit_button = "Create Item"
  if request.method == "POST":
    form = NewItemForm(request.POST, request.FILES)
    if form.is_valid():
      item = form.save(commit=False)
      item.created_by = request.user
      item.save()
      return redirect("item:detail", pk=item.id)
  else:
    form = NewItemForm()
  context = {"form": form, "form_type": form_type, 'submit_button': submit_button}
  return render(request, 'item/form.html', context)

@login_required
def edit_item(request, pk):
  form_type = "Edit Item"
  submit_button = "Update Item"
  item = get_object_or_404(Item, id=pk)
  if request.method == "POST":
    form = EditItemForm(data=request.POST, files=request.FILES, instance=item)
    if form.is_valid():
      form.save()
      return redirect("item:detail", pk=item.id)
  else:
    form = EditItemForm(instance=item)
  context = {"form": form, "form_type": form_type, 'submit_button': submit_button}
  return render(request, 'item/form.html', context)

@login_required
def delete(request, pk):
  item = get_object_or_404(Item, id=pk, created_by=request.user)
  if q := request.GET.get("q"):
    item.delete()
    return redirect("dashboard:index")
  context = {"item": item}
  return render(request, "item/delete.html", context)
