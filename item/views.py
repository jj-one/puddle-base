from django.shortcuts import render, get_object_or_404
from .models import Item
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
