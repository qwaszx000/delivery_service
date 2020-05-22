from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.utils import timezone
from django.http import JsonResponse

from api.models import *
from api.tools import models as tools


#########COURIER######################
# /api/coordinates/set/
def trackCourier(request):
	#check request method and is user manager
	if not request.method == "POST":
		return JsonResponse({'code': -1, 'msg': "Bad method.\nUse POST"})
	elif not request.user.courier.isCourier == True:
		return JsonResponse({'code': -3, 'msg': "Denied.\nOnly couriers allowed"})

	user = request.user
	user.courier.CoordinatesLongtitude = request.POST.get('longtitude')
	user.courier.CoordinatesLatitude = request.POST.get('latitude')
	user.courier.LastLoginDate = timezone.now()
	user.save()

	return JsonResponse({'code': 1, 'msg': "Coordinates sent successful"})

# /api/orders/courier_get/
def courierGetOrders(request):
	#check request method and is user manager or courier
	if not request.method == "GET":
		return JsonResponse({'code': -1, 'msg': "Bad method.\nUse GET"})
	elif not tools.get_user_type(request.user) in ['courier']:
		return JsonResponse({'code': -3, 'msg': "Denied.\nOnly couriers allowed"})


	courier = request.user.courier
	filtering_type = request.GET.get('filter', 'all')

	#Status can be: new, sent_to_kitchen, in_cook_process, in_delivery_process, delivered, rejected, delayed
	if filtering_type == 'all':
		orders = list(Order.objects.filter(Couriers__pk__contains=courier.pk).values())
	elif filtering_type in ['new', 'sent_to_kitchen', 'in_cook_process', 'in_delivery_process', 'delivered', 'rejected', 'delayed']:
		orders = Order.objects.filter(Couriers__pk__contains=courier.pk)
		orders = list(orders.filter(Status=filtering_type).values())
	else:
		return JsonResponse({'code': -4, 'msg': 'Bad filter'})

	return JsonResponse({'code': 1, 'msg': 'Send orders', 'orders': orders})

# /api/order/take/<order_id>
def takeOrder(request, order_id):
	pass

# /api/order/give/<order_id>
def giveOrder(request, order_id):
	pass

###############MANAGER################
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
	request.user.manager.LastLoginDate = timezone.now()
	request.user.save()

	return JsonResponse({'code': 1, 'msg': "BattaryCharge changed!"})

#manager confirms order
# /api/order/confirm/<order_id>
def confirmOrder(request, order_id):
	if not tools.get_user_type(request.user) in ['manager']:
		return JsonResponse({'code': -3, 'msg': "Denied.\nOnly managers allowed"})

	cookingTime = request.POST.get('time', 0)
	if cookingTime == 0:
		for orderPosition in OrderPosition.objects.filter(Order__pk=order_id):
			cookingTime += int(orderPosition.Restaurant.StandartCookingTime)

	order = Order.objects.get(pk=order_id)
	order.Status = "sent_to_kitchen"
	order.CookingTime = cookingTime
	order.save()

	return JsonResponse({'code': 1, 'msg': "Order confirmed"})

########MANAGER and COURIER###########
# /api/order/details/<order_id>
def getOrderDetails(request, order_id=1):
	#check is user manager or courier
	if not tools.get_user_type(request.user) in ['manager', 'courier']:
		return JsonResponse({'code': -3, 'msg': "Denied.\nOnly managers and couriers allowed"})

	try:
		order = list(Order.objects.filter(pk=order_id).values())[0]
	except IndexError:
		return JsonResponse({'code': -4, 'msg': "Order not found"})

	return JsonResponse({'code': 1, 'msg': "Send order", 'order': order})


#returns list of orders
# /api/orders/get/
def getOrders(request):
	#check request method and is user manager or courier
	if not request.method == "GET":
		return JsonResponse({'code': -1, 'msg': "Bad method.\nUse GET"})
	elif not tools.get_user_type(request.user) in ['manager', 'courier']:
		return JsonResponse({'code': -3, 'msg': "Denied.\nOnly managers and couriers allowed"})

	filtering_type = request.GET.get('filter', 'all')

	#Status can be: new, sent_to_kitchen, in_cook_process, in_delivery_process, delivered, rejected, delayed
	if filtering_type == 'all':
		orders = list(Order.objects.all().values())
	elif filtering_type in ['new', 'sent_to_kitchen', 'in_cook_process', 'in_delivery_process', 'delivered', 'rejected', 'delayed']:
		orders = list(Order.objects.filter(Status=filtering_type).values())
	else:
		return JsonResponse({'code': -4, 'msg': 'Bad filter'})

	return JsonResponse({'code': 1, 'msg': 'Send orders', 'orders': orders})

###########CLIENT#####################


##########EVERY USER##################
def loginUser(request):
	if not request.method == "POST":
		return JsonResponse({'code': -1, 'msg': "Bad method.\nUse Post"})

	#if empty input - set it to ''
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		#return session id in json
		#possibly can be useful
		sessionid = request.session.session_key
		return JsonResponse({'code': 1, 'msg': 'successful login', 'sessionid': sessionid})
	else:
		return JsonResponse({'code': -1, 'msg': 'login error!\nUser not found!'})

def logoutUser(request):
	if request.user.is_authenticated:
		logout(request)
		return JsonResponse({'code': 1, 'msg': 'successful logout'})
	else:
		return JsonResponse({'code': -2, 'msg': 'You are not logined'})

#returns type of current user manager, courier or client
def checkMyType(request):
	return JsonResponse({'code': 1, 'msg': tools.get_user_type(request.user)})