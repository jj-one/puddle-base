from django.urls import path
from .views import detail, new_item, delete, edit_item, items


app_name = 'item'
urlpatterns = [
  path("", items, name="items"),
  path('new/', new_item, name='new'),
  path('<int:pk>/', detail, name='detail'),
  path("delete/<int:pk>/", delete, name="delete"),
  path("edit/<int:pk>/", edit_item, name="edit"),
]