from django.contrib import admin
from .models import *

# Register your models here.
 
admin.site.register(Dish)
admin.site.register(Topping)
admin.site.register(Accompaniment)
admin.site.register(Modification)
admin.site.register(Taxe)
admin.site.register(Package)
admin.site.register(CuisineType)
admin.site.register(DishTag)

admin.site.register(Restaurant)
admin.site.register(RestaurantSectionMenu)
admin.site.register(Order)
admin.site.register(TimePeriod)
admin.site.register(OrderPosition)

admin.site.register(Client)
admin.site.register(DeliveryAddress)
admin.site.register(CreditCard)

admin.site.register(Manager)
admin.site.register(Courier)