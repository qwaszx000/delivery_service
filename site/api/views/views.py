from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import JsonResponse
from api.models import *
from api.tools.models import *

# Create your views here.

def loginUser(request):
	if not request.method == "POST":
		return JsonResponse({'code': -1, 'msg': "Bad method.\nUse Post"})

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
	return JsonResponse({'code': 1, 'msg': get_user_type(request.user)})