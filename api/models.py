from django.db import models

# Create your models here.

class Dish(models.Model):
	pass

class Restaurant(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128)
	Address = models.CharField(max_length=512)
	CoordinatesLongtitude = models.FloatField()
	CoordinatesLatitude = models.FloatField()
	Phone = models.CharField(max_length=16)
	DiscountGiven = models.BooleanField()
	StandartCookingTime = models.SmallIntegerField()
	MoreInfoEnglish = models.TextField()
	MoreInfoSecond = models.TextField()
	SeoSectionEnglish = models.TextField()
	SeoSectionSecond = models.TextField()
	Type = models.CharField(max_length=12)#simple/dark-kitchen/both
	#TypeOfCusine = 
	#SliderImgBigEng = 
	#SliderImgSmallEng = 
	#SliderImgBigSecond = 
	#SliderImgSmallSecond = 

#additional ingredient
class Topping(models.Model):
	pass

#snack
class Accompaniments(models.Model)
	pass

class Order(models.Model):
	pass

class TimePeriod(models.Model):
	pass

class Client(models.Model):
	pass

class DeliveryAddress(models.Model):
	#if client removed - remove address releated with him
	#many DeliveryAddress to one Client
	Client = models.ForeignKey(Client, on_delete=models.CASCADE)

class CreditCard(models.Model):
	#if client removed - remove CreditCard releated with him
	#many CreditCard to one Client
	Client = models.ForeignKey(Client, on_delete=models.CASCADE)
