from django.urls import path
from .views import detail, new_item


app_name = 'item'
urlpatterns = [
  path('new/', new_item, name='new'),
  path('<int:pk>/', detail, name='detail'),
]