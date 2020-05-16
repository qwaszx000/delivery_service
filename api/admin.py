from django.contrib import admin
from delivery_django.api.models import *

# Register your models here.
 
admin.site.register(Dish)
admin.site.register(Restaurant)
admin.site.register(Topping)
admin.site.register(Accompaniments)
admin.site.register(Order)
admin.site.register(TimePeriod)
admin.site.register(Client)
admin.site.register(DeliveryAddress)
admin.site.register(CreditCard)