from django.urls import path
from .views import views

urlpatterns = [
	path('login/', views.loginUser, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	path('check/', views.checkMyType, name='checkMyType'),
]