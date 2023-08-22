from django.urls import path
from orderfood.views import OrderListView, OrderDetailView,FoodListView,FoodDetailView

urlpatterns = [
    path('order/', OrderListView.as_view(), name='orders'),
    path('order/<int:pk>/',OrderDetailView.as_view(),name="order-detail"),
    path('food/', FoodListView.as_view(), name='foods'),
    path('food/<int:pk>/',FoodDetailView.as_view(),name="food-detail"),
]
