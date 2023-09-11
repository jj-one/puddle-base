from django.shortcuts import render

# Create your views here.
def index(request):
  context = {}
  return render(request, 'core/index.html', context)

def contact(request):
  context = {}
  return render(request, 'core/contact.html', context)