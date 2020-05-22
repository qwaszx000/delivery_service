from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from api.models import *

# Create your views here.
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
