from django.shortcuts import render
from django.http import JsonResponse
from api.models import *
from django.contrib.auth.models import User
from api.tools import models as tools
#import json

# Create your views here.
# api calls allowed only for managers

#sets user type by name
# /api/type/set/
def setUserType(request):
	#check request method and is user manager
	if not request.method == "POST":
		return JsonResponse({'code': -1, 'msg': "Bad method.\nUse Post"})
	elif not request.user.manager.isManager == True:
		return JsonResponse({'code': -3, 'msg': "Denied.\nOnly managers allowed"})

	#if empty input - set it to ''
	targetName = request.POST.get('username', '')
	newType = request.POST.get('type', '')

	try:
		user = User.objects.get(username=targetName)
	except User.DoesNotExist:
		return JsonResponse({'code': -5, 'msg': 'user not found'})

	if tools.setUserType(user, newType) == -1:
		JsonResponse({'code': -4, 'msg': 'bad user type'})

	user.save()

	return JsonResponse({'code': 1, 'msg': 'success', 'type': newType})

#returns list of orders
# /api/orders/get/
def getOrders(request):
	#check request method and is user manager
	if not request.method == "GET":
		return JsonResponse({'code': -1, 'msg': "Bad method.\nUse GET"})
	elif not request.user.manager.isManager == True:
		return JsonResponse({'code': -3, 'msg': "Denied.\nOnly managers allowed"})

	filtering_type = request.GET.get('filter', 'all')

	#Status can be: new, sent_to_kitchen, in_cook_process, in_delivery_process, delivered, rejected, delayed
	if filtering_type == 'all':
		orders = list(Order.objects.all().values())
	elif filtering_type in ['new', 'sent_to_kitchen', 'in_cook_process', 'in_delivery_process', 'delivered', 'rejected', 'delayed']:
		orders = list(Order.objects.filter(Status=filtering_type).values())
	else:
		return JsonResponse({'code': -4, 'msg': 'Bad filter'})

	return JsonResponse({'code': 1, 'msg': 'Send orders', 'orders': orders})

#managers app sends this request each 10 minutes
# /api/charge/set/
def setBattaryCharge(request):
	#check request method and is user manager
	if not request.method == "POST":
		return JsonResponse({'code': -1, 'msg': "Bad method.\nUse Post"})
	elif not request.user.manager.isManager == True:
		return JsonResponse({'code': -3, 'msg': "Denied.\nOnly managers allowed"})

	#default value - 100%
	charge = request.POST.get('charge', 100)

	request.user.manager.BattaryCharge = int(charge)
	request.user.save()

	return JsonResponse({'code': 1, 'msg': "BattaryCharge changed!"})

# /api/order/details/<order_id>
def getOrderDetails(request, order_id=1):
	#check is user manager
	if not request.user.manager.isManager == True:
		return JsonResponse({'code': -3, 'msg': "Denied.\nOnly managers allowed"})

	order = list(Order.objects.filter(pk=order_id).values())[0]

	return JsonResponse({'code': 1, 'msg': "Send order", 'order': order})