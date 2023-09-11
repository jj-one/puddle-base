from django.shortcuts import render
from item.models import Category, Item

# Create your views here.
def index(request):
  categories = Category.objects.all()
  items = Item.objects.filter(is_sold=False)[:6]
  context = {'items': items, 'categories': categories}
  return render(request, 'core/index.html', context)

def contact(request):
  context = {}
  return render(request, 'core/contact.html', context)