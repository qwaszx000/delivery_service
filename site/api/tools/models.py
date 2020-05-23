#Contains tools that may be useful in api models
from api.models import *

### user
def get_user_type(user):
	if user.manager.isManager == True:
		return "manager"
	elif user.courier.isCourier == True:
		return "courier"
	else:
		return "client"

def setUserType(user, newtype):
	if newtype == "manager":
		user.manager.isManager = True
		user.courier.isCourier = False
		user.client.isClient = False
	elif newtype == "courier":
		user.manager.isManager = False
		user.courier.isCourier = True
		user.client.isClient = False
	elif newtype == "client":
		user.manager.isManager = False
		user.courier.isCourier = False
		user.client.isClient = True
	else:
		return -1

### orders
# filter options: courier, status
def getOrdersList(courier_pk=-1, status='all', timeperiod_pk=-1):
	if status not in ['all', 'new', 'sent_to_kitchen', 'in_cook_process', 'in_delivery_process', 'delivered', 'rejected', 'delayed']:
		return -1

	if not courier_pk == -1:
		orders = Order.objects.filter(Couriers__pk__contains=courier_pk)

	if not timeperiod_pk == -1:
		orders = orders.filter(TimePeriod__pk__contains=timeperiod_pk)

	if not filtering_type == 'all':
		orders = orders.filter(Status=filtering_type)

	return list(orders.values())
