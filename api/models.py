from django.db import models

# Create your models here.

class Dish(models.Model):
	#if Restaurant removed - remove Dish releated with him
	#many Dish to one Restaurant
	Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	DeliveryPrice = models.FloatField()

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
	SliderImgBigEng = models.ImageField(upload_to="uploads/eng/big/")
	SliderImgSmallEng = models.ImageField(upload_to="uploads/eng/small/")
	SliderImgBigSecond = models.ImageField(upload_to="uploads/second/big/")
	SliderImgSmallSecond = models.ImageField(upload_to="uploads/second/small")

#additional ingredient
class Topping(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128)
	PricePurchase = models.FloatField()
	PriceSell = models.FloatField()

#snack
class Accompaniments(models.Model)
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128)
	PricePurchase = models.FloatField()
	PriceSell = models.FloatField()

class Order(models.Model):
	pass

class TimePeriod(models.Model):
	# use json.
	# example "[1, 4]"
	# 0 - Monday
	# 1 - Tuesday
	# 2 - Wednesday
	# 3 - Thursday
	# 4 - Friday
	# 5 - Saturday
	# 6 - Sunday
	DaysOfWeek = models.CharField(max_length=128)

# https://habr.com/ru/post/313764/
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
#using one to one connection
class Client(models.Model):
	User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	Name = models.CharField(max_length=128)
	Surname = models.CharField(max_length=128)
	Phone = models.CharField(max_length=16)
	#auto_now_add=True 
	#Automatically set the field to now when the object is first created.
	RegisterData = models.DateTimeField(auto_now_add=True)
	LastLoginDate = models.DateTimeField(auto_now_add=True)

class DeliveryAddress(models.Model):
	#if client removed - remove address releated with him
	#many DeliveryAddress to one Client
	Client = models.ForeignKey(Client, on_delete=models.CASCADE)
	Street = models.CharField(max_length=128)
	HouseName = models.CharField(max_length=128)
	Flat = models.CharField(max_length=128)
	Floor = models.CharField(max_length=128)
	Comment = models.TextField()
	AddingDate = models.DateTimeField(auto_now_add=True)

class CreditCard(models.Model):
	#if client removed - remove CreditCard releated with him
	#many CreditCard to one Client
	Client = models.ForeignKey(Client, on_delete=models.CASCADE)
	CardToken = models.CharField(max_length=256)
	CardType = models.CharField(max_length=128) #Visa/mastercard/american express
	LastFourDigits = models.CharField(max_length=4)
	AddingDate = models.DateTimeField(auto_now_add=True)
