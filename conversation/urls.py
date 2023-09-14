from django.urls import path

from .views import new_conversation, inbox, detail

app_name = "conversation"

urlpatterns = [
  path("", inbox, name="inbox"),
  path('<int:convers_id>/', detail, name="detail"),
  path('new/<int:item_id>/', new_conversation, name="new"),
]