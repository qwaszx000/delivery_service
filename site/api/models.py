from django.db import models
from django.conf import settings

# Create your models here.

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
	LastLoginDate = models.DateTimeField(auto_now=True)

class CuisineType(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128)

class DishTag(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128)

class RestaurantSectionMenu(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128)

class Taxe(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128)
	ValuePercent = models.FloatField()

class Package(models.Model):
	Name = models.CharField(max_length=128)
	Price = models.FloatField()
	SalePrice = models.FloatField()

#example - roasting level for meat
class Modification(models.Model):
	EnglishName = models.CharField(max_length=128)#roasting level for meat
	SecondName = models.CharField(max_length=128)  
	Value = models.CharField(max_length=128) #medium

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
	ExpireDate = models.DateTimeField()

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

	# use format "hours:minuts:seconds"
	StartTime = models.CharField(max_length=128)
	StopTime = models.CharField(max_length=128)

class Restaurant(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128)
	#geo
	Address = models.CharField(max_length=512)
	CoordinatesLongtitude = models.FloatField()
	CoordinatesLatitude = models.FloatField()

	Phone = models.CharField(max_length=16)
	DiscountGiven = models.BooleanField()
	StandartCookingTime = models.SmallIntegerField()
	#more info
	MoreInfoEnglish = models.TextField()
	MoreInfoSecond = models.TextField()
	#seo
	SeoSectionEnglish = models.TextField()
	SeoSectionSecond = models.TextField()
	#types
	Type = models.CharField(max_length=12)#simple/dark-kitchen/both
	TypesOfCusine = models.ManyToManyField(CuisineType)
	SectionMenus = models.ManyToManyField(RestaurantSectionMenu)
	#imgs
	SliderImgBigEng = models.ImageField(upload_to="uploads/img/eng/big/")
	SliderImgSmallEng = models.ImageField(upload_to="uploads/img/eng/small/")
	SliderImgBigSecond = models.ImageField(upload_to="uploads/img/second/big/")
	SliderImgSmallSecond = models.ImageField(upload_to="uploads/img/second/small")

# https://habr.com/ru/post/313764/
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
#using one to one connection
class Manager(models.Model):
	User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	#One manager - one restaurant
	Restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
	BattaryCharge = models.SmallIntegerField()
	LastLoginDate = models.DateTimeField(auto_now=True)

# https://habr.com/ru/post/313764/
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
#using one to one connection
class Courier(models.Model):
	User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	Color = models.CharField(max_length=7) #example "#000000"
	LastLoginDate = models.DateTimeField(auto_now=True)

#additional ingredient
class Topping(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128)
	PricePurchase = models.FloatField()
	PriceSell = models.FloatField()
	Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

#snack
class Accompaniment(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128)
	PricePurchase = models.FloatField()
	PriceSell = models.FloatField()
	Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Dish(models.Model):
	#if Restaurant removed - remove Dish releated with him
	#many Dish to one Restaurant
	Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	DeliveryPrice = models.FloatField()

	Tags = models.ManyToManyField(DishTag)
	
	#cost
	PurchasePrice = models.FloatField()
	SalePrice = models.FloatField()
	Taxe = models.ForeignKey(Taxe, on_delete=models.CASCADE)

	#modificators
	Accompaniments = models.ManyToManyField(Accompaniment)
	Toppings = models.ManyToManyField(Topping)
	Modifications = models.ManyToManyField(Modification)
	Packages = models.ManyToManyField(Package)

	#limits
	LimitPerOrder = models.SmallIntegerField()
	TimePeriod = models.OneToOneField(TimePeriod, on_delete=models.CASCADE)

	DarkKitchen = models.BooleanField()

	#img
	ImgPopup = models.ImageField(upload_to="uploads/img/popup/")
	ImgMenuPage = models.ImageField(upload_to="uploads/img/menu_page/")

#contains OrderPosition
class Order(models.Model):
	#if client removed - remove Order releated with him
	#many Order to one Client
	Client = models.ForeignKey(Client, on_delete=models.CASCADE)

	#if paytype is creditcard - payinfo will get card id
	PayType = models.CharField(max_length=128)
	PayInfo = models.CharField(max_length=128)
	#many orders to one delivery address
	DeliveryAddress = models.ForeignKey(DeliveryAddress, on_delete=models.SET_NULL, null=True)
	#чаевые
	TipsCount = models.FloatField()
	TotalCost = models.FloatField()
	DeliveryCost = models.FloatField()

	AddingDate = models.DateTimeField(auto_now_add=True)
	#на когда заказали
	OnWhenDate = models.DateTimeField()
	DeliveredDate = models.DateTimeField()

	TimePeriod = models.OneToOneField(TimePeriod, on_delete=models.CASCADE)
	CourierTakedMoney = models.OneToOneField(Courier, on_delete=models.SET_NULL, null=True)

	Status = models.CharField(max_length=128)
	#Status can be: new, sent_to_kitchen, in_cook_process, in_delivery_process, delivered, rejected, delayed

#for 1 dish
class OrderPosition(models.Model):
	Dish = models.OneToOneField(Dish, on_delete=models.CASCADE)
	#many OrderPosition to one order and restourants
	Order = models.ForeignKey(Order, on_delete=models.CASCADE)
	Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	#price
	BuyPrice = models.FloatField()
	SellPrice = models.FloatField()
	Discount = models.FloatField()
	Taxe = models.ForeignKey(Taxe, on_delete=models.CASCADE)

	Courier = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True)

	#datetimes
	AddingDate = models.DateTimeField(auto_now_add=True)
	SendToRestourantDate = models.DateTimeField(auto_now=True)
	RestourantConfirmDate = models.DateTimeField(auto_now=True)
	RestourantDoneDate = models.DateTimeField(auto_now=True)
	CourierTakedDate = models.DateTimeField(auto_now=True)
	CourierDeliveredDate = models.DateTimeField(auto_now=True)

	Status = models.CharField(max_length=128)
	#Status can be: new, sent_to_kitchen, in_cook_process, in_delivery_process, delivered, rejected, delayed


