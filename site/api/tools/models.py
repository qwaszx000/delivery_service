#Contains tools that may be useful in api models
from api.models import *
from django.conf import settings

#settings.AUTH_USER_MODEL
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