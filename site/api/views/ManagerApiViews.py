from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.models import User
from api.models import *
from api.tools import models as tools

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