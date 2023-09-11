from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):

  name = models.CharField(max_length=255)

  class Meta:
    ordering = ('name',)

  def __str__(self):
    return self.name
  
class Item(models.Model):

  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
  name = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  price = models.FloatField()
  image = models.ImageField(upload_to='item_images', null=True, blank=True)
  is_sold = models.BooleanField(default=False)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-created', 'category', 'name')

  def __str__(self):
    return f"{self.name} (in {self.category})"
