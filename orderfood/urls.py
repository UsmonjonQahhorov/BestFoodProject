from django.urls import path
from orderfood import views


urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("orders/list/",views.OrdersListView.as_view(),name="orders-list"),
    path("orders/create/",views.OrdersCreateView.as_view(),name="orders-create"),
    path("orders/<int:pk>/detail/",views.OrdersDetailView.as_view(),name="orders-detail"),
    path("orders/<int:pk>/update/",views.OrdersDetailView.as_view(),name="orders-update"),
    path("orders/<int:pk>/delete/",views.orders_delete, name="orders-delete"),
    path("food/list/",views.FoodsListView.as_view(),name="food-list"),
    path("food/create/",views.FoodsCreateView.as_view(),name="food-create"),
    path("food/<int:pk>/detail/",views.FoodsDetailView.as_view(),name="food-detail"),
    path("food/<int:pk>/update/",views.FoodsUpdateView.as_view(),name="food-update"),
    path("food/<int:pk>/delete/",views.foods_delete, name="food-delete"),
]









# urlpatterns = [
#     path('order/', OrderListView.as_view(), name='orders'),
#     path('order/<int:pk>/',OrderDetailView.as_view(),name="order-detail"),
#     path('food/', FoodListView.as_view(), name='foods'),
#     path('food/<int:pk>/',FoodDetailView.as_view(),name="food-detail"),
# ]
