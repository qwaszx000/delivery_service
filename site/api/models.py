from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# https://habr.com/ru/post/313764/
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
#using one to one connection
class Client(models.Model):
	User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	Name = models.CharField(max_length=128, null=True)
	Surname = models.CharField(max_length=128, default="", null=True, blank=True)
	Phone = models.CharField(max_length=16, null=True)
	#auto_now_add=True 
	#Automatically set the field to now when the object is first created.
	RegisterData = models.DateTimeField(auto_now_add=True)
	LastLoginDate = models.DateTimeField(auto_now=True)

	isClient = models.BooleanField(default=True)

class CuisineType(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128, default="", null=True, blank=True)

class DishTag(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128, default="", null=True, blank=True)

class RestaurantSectionMenu(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128, default="", null=True, blank=True)

class Taxe(models.Model):
	EnglishName = models.CharField(max_length=128)
	SecondName = models.CharField(max_length=128, default="", null=True, blank=True)
	ValuePercent = models.FloatField()

class Package(models.Model):
	Name = models.CharField(max_length=128)
	Price = models.FloatField()
	SalePrice = models.FloatField()

#example - roasting level for meat
class Modification(models.Model):
	EnglishName = models.CharField(max_length=128)#roasting level for meat
	SecondName = models.CharField(max_length=128, default="", null=True, blank=True)  
	Value = models.CharField(max_length=128) #medium

class DeliveryAddress(models.Model):
	#if client removed - remove address releated with him
	#many DeliveryAddress to one Client
	Client = models.ForeignKey(Client, on_delete=models.CASCADE)
	Street = models.CharField(max_length=128)
	HouseName = models.CharField(max_length=128)
	Flat = models.CharField(max_length=128)
	Floor = models.CharField(max_length=128)
	Comment = models.TextField(default="", null=True, blank=True)
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
	CoordinatesLongtitude = models.FloatField(null=True, blank=True)
	CoordinatesLatitude = models.FloatField(null=True, blank=True)

	Phone = models.CharField(max_length=16)
	DiscountGiven = models.FloatField()
	StandartCookingTime = models.SmallIntegerField()
	#more info
	MoreInfoEnglish = models.TextField(default="", null=True, blank=True)
	MoreInfoSecond = models.TextField(default="", null=True, blank=True)
	#seo
	SeoSectionEnglish = models.TextField(default="", null=True, blank=True)
	SeoSectionSecond = models.TextField(default="", null=True, blank=True)
	#types
	Type = models.CharField(max_length=12, default="simple")#simple/dark-kitchen/both
	TypesOfCusine = models.ManyToManyField(CuisineType, blank=True)
	SectionMenus = models.ManyToManyField(RestaurantSectionMenu, blank=True)
	#imgs
	SliderImgBigEng = models.ImageField(upload_to="uploads/img/eng/big/", null=True, blank=True)
	SliderImgSmallEng = models.ImageField(upload_to="uploads/img/eng/small/", null=True, blank=True)
	SliderImgBigSecond = models.ImageField(upload_to="uploads/img/second/big/", null=True, blank=True)
	SliderImgSmallSecond = models.ImageField(upload_to="uploads/img/second/small", null=True, blank=True)

# https://habr.com/ru/post/313764/
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
#using one to one connection
class Manager(models.Model):
	User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	#One manager - one restaurant
	Restaurant = models.OneToOneField(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
	BattaryCharge = models.SmallIntegerField(default=100, null=True, blank=True)
	LastLoginDate = models.DateTimeField()

	isManager = models.BooleanField(default=False)

# https://habr.com/ru/post/313764/
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/
#using one to one connection
class Courier(models.Model):
	User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	Color = models.CharField(max_length=7, default="#555555", null=True, blank=True) #example "#000000"
	LastLoginDate = models.DateTimeField()

	CoordinatesLongtitude = models.FloatField(null=True, blank=True)
	CoordinatesLatitude = models.FloatField(null=True, blank=True)


	isCourier = models.BooleanField(default=False)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user(sender, instance, created, **kwargs):
	if created:
		Client.objects.create(User=instance)
		Manager.objects.create(User=instance)
		Courier.objects.create(User=instance)
		ShopCart.objects.create(Client=instance.client)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user(sender, instance, **kwargs):
	try:
		instance.client.save()
		instance.manager.save()
		instance.courier.save()
	#if user dont have client, manager and courier models
	except Exception:
		Client.objects.create(User=instance)
		Manager.objects.create(User=instance)
		Courier.objects.create(User=instance)

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

	Tags = models.ManyToManyField(DishTag, blank=True)
	
	#cost
	PurchasePrice = models.FloatField()
	SalePrice = models.FloatField()
	Taxe = models.ForeignKey(Taxe, on_delete=models.CASCADE)

	#modificators
	Accompaniments = models.ManyToManyField(Accompaniment, blank=True)
	Toppings = models.ManyToManyField(Topping, blank=True)
	Modifications = models.ManyToManyField(Modification, blank=True)
	Packages = models.ManyToManyField(Package, blank=True)

	#limits
	LimitPerOrder = models.SmallIntegerField()
	TimePeriod = models.OneToOneField(TimePeriod, on_delete=models.CASCADE)

	DarkKitchen = models.BooleanField()

	#img
	ImgPopup = models.ImageField(upload_to="uploads/img/popup/", null=True, blank=True)
	ImgMenuPage = models.ImageField(upload_to="uploads/img/menu_page/", null=True, blank=True)

#contains OrderPosition
class Order(models.Model):
	#if client removed - remove Order releated with him
	#many Order to one Client
	Client = models.ForeignKey(Client, on_delete=models.CASCADE)

	#if paytype is creditcard - payinfo will get card id
	PayType = models.CharField(max_length=128, null=True, blank=True)
	PayInfo = models.CharField(max_length=128, null=True, blank=True)
	#many orders to one delivery address
	DeliveryAddress = models.ForeignKey(DeliveryAddress, on_delete=models.SET_NULL, null=True, blank=True)
	#чаевые
	TipsCount = models.FloatField()
	TotalCost = models.FloatField()
	DeliveryCost = models.FloatField()

	AddingDate = models.DateTimeField(auto_now_add=True)
	#на когда заказали
	OnWhenDate = models.DateTimeField()
	DeliveredDate = models.DateTimeField()

	TimePeriod = models.OneToOneField(TimePeriod, on_delete=models.CASCADE)
	Couriers = models.ManyToManyField(Courier, blank=True)
	Status = models.CharField(max_length=128, default="new")
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

	Courier = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True, blank=True)

	#datetimes
	AddingDate = models.DateTimeField(auto_now_add=True)
	SendToRestourantDate = models.DateTimeField(auto_now=True)
	RestourantConfirmDate = models.DateTimeField(auto_now=True)
	RestourantDoneDate = models.DateTimeField(auto_now=True)
	CourierTakedDate = models.DateTimeField(auto_now=True)
	CourierDeliveredDate = models.DateTimeField(auto_now=True)

	Status = models.CharField(max_length=128, default="new")
	#Status can be: new, sent_to_kitchen, in_cook_process, in_delivery_process, delivered, rejected, delayed


class ShopCart(models.Model):
	Client = models.OneToOneField(Client, on_delete=models.CASCADE)
	Dishs = models.ManyToManyField(Dish, blank=True)