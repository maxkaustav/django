from django.db import models

# Create your models here.
class Customer(models.Model):
	"""
	name:name of user
	phone: phone number
	date: date
	email: emailid"""
	name=models.CharField(max_length=200,null=True)#string input
	phone=models.CharField(max_length=10, help_text="enter 10 digit mobile number",null=True,unique=True)
	date=models.DateTimeField(auto_now=False, auto_now_add=True)#auto time
	email=models.EmailField(max_length=254,null=True)#email validation

	def __str__(self):
		return self.name # visual for data in table to user

class Products(models.Model):
	"""
	name:name of user
	price:  number
	date: date
	category: product"""
	CATEGORY=[
		('Indoor','Indoor'),
		('Outdoor', 'Outdoor')
	]
	name=models.CharField(max_length=200,null=True)#string input
	price=models.FloatField(null=True)
	category=models.CharField(max_length=10,choices=CATEGORY,null=True)
	date=models.DateTimeField(auto_now=False, auto_now_add=True)#auto time
	description=models.CharField(max_length=10,null=True)
	def __str__(self):
		return self.name # visual for data in table to user

class Order(models.Model):
	"""
	name:name of user
	price:  number
	date: date
	category: product"""
	ORDER=[
		('P','Pending'),
		('O', 'Out for delivery'),
		('D','Dlivered')
	]

	status=models.CharField(max_length=10,choices=ORDER,null=True)
	date=models.DateTimeField(auto_now=False, auto_now_add=True)#auto time
	def __str__(self):
		return self.status# visual for data in table to user
	