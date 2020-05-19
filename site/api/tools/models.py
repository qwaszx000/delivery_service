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