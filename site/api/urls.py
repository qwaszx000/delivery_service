from django.urls import path
from .views import UserApiViews

urlpatterns = [
	###auth
	path('login/', UserApiViews.loginUser, name='login'),
	path('logout/', UserApiViews.logoutUser, name='logout'),
	###type
	path('type/check/', UserApiViews.checkMyType, name='checkMyType'),
	path('type/set/', UserApiViews.setUserType, name='setUserType'),
	###manager&courier info
	path('charge/set/', UserApiViews.setBattaryCharge, name="setBattaryCharge"),
	path('coordinates/set/', UserApiViews.trackCourier, name="trackCourier"),
	###orders
	path('order/details/<int:order_id>', UserApiViews.getOrderDetails, name="getOrderDetails"),
	path('orders/get/', UserApiViews.getOrders, name="getOrders"),
	path('order/take/<int:order_id>', UserApiViews.takeOrder, name="takeOrder"),
	path('order/give/<int:order_id>', UserApiViews.giveOrder, name="giveOrder"),
	path('order/confirm/<int:order_id>', UserApiViews.confirmOrder, name="confirmOrder"),
	###cart
]