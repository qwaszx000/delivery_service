from django.shortcuts import render
from django.http import JsonResponse
from api.models import *

# Create your views here.

def index(request):
	context = {
		'test': 'test',
	}
	return JsonResponse(context) #render(request, 'index.html', context)