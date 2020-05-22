from django.urls import path
from .views import views
from .views import ManagerApiViews
from .views import OrdersApiViews
from .views import CourierApiViews

urlpatterns = [
	###auth
	path('login/', views.loginUser, name='login'),
	path('logout/', views.logoutUser, name='logout'),
	###edit user
	path('type/check/', views.checkMyType, name='checkMyType'),
	path('type/set/', ManagerApiViews.setUserType, name='setUserType'),
	path('charge/set/', ManagerApiViews.setBattaryCharge, name="setBattaryCharge"),
	path('coordinates/set/', CourierApiViews.trackCourier, name="trackCourier"),
	###orders
	path('order/details/<int:order_id>', OrdersApiViews.getOrderDetails, name="getOrderDetails"),
	path('orders/get/', OrdersApiViews.getOrders, name="getOrders"),
]