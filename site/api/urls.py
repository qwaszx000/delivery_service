from django.urls import path
from .views import views
from .views import ManagerApiViews

urlpatterns = [
	path('login/', views.loginUser, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	path('type/check/', views.checkMyType, name='checkMyType'),
	path('type/set/', ManagerApiViews.setUserType, name='setUserType'),
	path('order/details/<int:order_id>', ManagerApiViews.getOrderDetails, name="getOrderDetails"),
	path('orders/get/', ManagerApiViews.getOrders, name="getOrders"),
	path('charge/set/', ManagerApiViews.setBattaryCharge, name="setBattaryCharge"),
]