from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_lists(models.Model):
	list_name = models.CharField(max_length=30)
	list_owner = models.ForeignKey(User, on_delete=models.CASCADE)

class list_item(models.Model):
	item_name = models.CharField(max_length=100)
	item_amount = models.FloatField(default='0.0')
	item_unit = models.CharField(max_length=20, default=" ")
	item_list = models.ForeignKey(user_lists, on_delete=models.CASCADE)