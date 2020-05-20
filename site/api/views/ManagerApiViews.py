from django.shortcuts import render
from django.http import JsonResponse
from api.models import *
from django.contrib.auth.models import User

# Create your views here.

def setUserType(request):
	if not request.method == "POST":
		return JsonResponse({'code': -1, 'msg': "Bad method.\nUse Post"})
	elif:
		if not request.user.manager.isManager == True:
			return JsonResponse({'code': -3, 'msg': "Denied.\nOnly managers allowed"})

	targetName = request.POST.get('username')
	newType = request.POST.get('type')

	try:
		user = User.objects.get(username=targetName)
	except User.DoesNotExist:
		return JsonResponse({'code': -5, 'msg': 'user not found'})

	if newType == "manager":
		user.manager.isManager = True
		user.courier.isCourier = False
		user.client.isClient = False
	elif newType == "courier":
		user.manager.isManager = False
		user.courier.isCourier = True
		user.client.isClient = False
	elif newType == "client":
		user.manager.isManager = False
		user.courier.isCourier = False
		user.client.isClient = True
	else:
		return JsonResponse({'code': -4, 'msg': 'bad user type'})

	user.save()

	return JsonResponse({'code': 1, 'msg': 'success', 'type': newType})