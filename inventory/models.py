from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	product_name = models.CharField(max_length=15)
	product_number = models.IntegerField()
	product_quantity = models.IntegerField()
	date_recieved = models.DateField()
	description = models.CharField(max_length=40)
	Price =  models.FloatField()
	stocks = models.IntegerField()
	production_date = models.DateField()
	expiry_date = models.DateTimeField()
	expired = models.BooleanField(default=False)

	def __str__(self) -> str:
		return self.product_name
	
	def save(self, *args, **kwargs):
		self.expired = self.expiry_date <= timezone.now()
		super().save(*args, **kwargs)
    
	class Meta:
		ordering = ['date_recieved']

	
class Staff(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	staff_id = models.IntegerField()
	staff_name = models.CharField(max_length=10)
	gender = models.CharField(max_length=10)
	age = models.IntegerField()
	date_of_birth = models.DateField()
	address = models.CharField(max_length=500)
	contact = models.IntegerField()
	date_of_entry = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return self.user.username
	class Meta:
		ordering = ['-date_of_entry']