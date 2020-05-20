from django.urls import path
from .views import views
from .views import ManagerApiViews

urlpatterns = [
	path('login/', views.loginUser, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	path('type/check/', views.checkMyType, name='checkMyType'),
	path('type/set/', ManagerApiViews.setUserType, name='setUserType'),
]