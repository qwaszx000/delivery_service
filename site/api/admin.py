from django.contrib import admin
from .models import *

# Register your models here.
 
class ShowIdAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)

admin.site.register(Dish, ShowIdAdmin)
admin.site.register(Topping, ShowIdAdmin)
admin.site.register(Accompaniment, ShowIdAdmin)
admin.site.register(Modification, ShowIdAdmin)
admin.site.register(Taxe, ShowIdAdmin)
admin.site.register(Package, ShowIdAdmin)
admin.site.register(CuisineType, ShowIdAdmin)
admin.site.register(DishTag, ShowIdAdmin)

admin.site.register(Restaurant, ShowIdAdmin)
admin.site.register(RestaurantSectionMenu, ShowIdAdmin)
admin.site.register(Order, ShowIdAdmin)
admin.site.register(TimePeriod, ShowIdAdmin)
admin.site.register(OrderPosition, ShowIdAdmin)

admin.site.register(DeliveryAddress, ShowIdAdmin)
admin.site.register(CreditCard, ShowIdAdmin)
admin.site.register(ShopCart, ShowIdAdmin)

admin.site.register(Client, ShowIdAdmin)
admin.site.register(Manager, ShowIdAdmin)
admin.site.register(Courier, ShowIdAdmin)