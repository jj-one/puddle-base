from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import NewItemForm, EditItemForm
# Create your views here.

def detail(request, pk):
  item = get_object_or_404(Item, id=pk)
  try:
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=item.id)[:3]
  except Exception as _:
    context = {"item": item}
    return render(request, 'item/detail.html', context)
  
  context = {"item": item, "related_items": related_items}
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
