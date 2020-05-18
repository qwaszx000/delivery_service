from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import JsonResponse
from api.models import *

# Create your views here.

def loginUser(request):
	if request.method not == "POST":
		return JsonResponse({'code': -1, 'msg': "Bad method.\nUse Post"})

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return JsonResponse({'code': 1, 'msg': 'successful login'})
	else:
		return JsonResponse({'code': -1, 'msg': 'login error!\nUser not found!'})

def logoutUser(request):
	logout(request)
	return JsonResponse({'code': 1, 'msg': 'successful logout'})