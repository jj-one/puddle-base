from django.contrib import admin
from .models import Category, Item

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

  list_display = ('id', 'name')

class ItemAdmin(admin.ModelAdmin):

  list_display = ('name', 'category', 'price', 'created')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
