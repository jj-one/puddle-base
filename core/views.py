from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm

# Create your views here.
def index(request):
  categories = Category.objects.all()
  items = Item.objects.filter(is_sold=False)[:6]
  context = {'items': items, 'categories': categories}
  return render(request, 'core/index.html', context)

def contact(request):
  context = {}
  return render(request, 'core/contact.html', context)

def signup(request):
  if request.method == "POST":
    form = SignupForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("core:login")
  else:
    form = SignupForm()
  context = {"form": form}
  return render(request, 'core/signup.html', context)