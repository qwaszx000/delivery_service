from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.models import User
from api.models import *
from api.tools import models as tools

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


# /api/order/details/<order_id>
def getOrderDetails(request, order_id=1):
	#check is user manager or courier
	if not tools.get_user_type(request.user) in ['manager', 'courier']:
		return JsonResponse({'code': -3, 'msg': "Denied.\nOnly managers and couriers allowed"})

	order = list(Order.objects.filter(pk=order_id).values())[0]

	return JsonResponse({'code': 1, 'msg': "Send order", 'order': order})

def confirmOrder(request, order_id):
	pass