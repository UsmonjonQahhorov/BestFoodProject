from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orderfood.models import Order,Food
from orderfood.serializers import OrderSerializer,FoodSerializer
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view





from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import get_object_or_404,redirect
from django.db.models import Q
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView
)

from orderfood.forms import OrderForm,FoodForm
from orderfood.models import Order

class IndexView(TemplateView):
    template_name = 'head.html'


class OrdersListView(ListView):
    model = Order
    template_name = 'order/list.html'
    context_object_name = "orders"



    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        head = self.request.GET.get('head')
        order_id = self.request.GET.get('order_id')

        if search:
            queryset = queryset.filter(
                Q(name__contains = search) | Q(description__contains = search)
            )
        if head:
            queryset = queryset.filter(
                head = head
            )
        if order_id:
            queryset = queryset.filter(
                order_id = order_id
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.all()
        context["search"] = self.request.GET.get('search',"")

        return context


class OrdersCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = '/orders/list/'
    template_name = 'order/form.html'

class OrdersUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    success_url = '/orders/list'
    template_name = 'order/form.html'

class OrdersDetailView(DetailView):
    model = Order
    template_name = 'order/detail.html'
    context_object_name = "orders"

def orders_delete(request,pk):
    orders = get_object_or_404(Order,pk=pk)
    orders.delete()
    return redirect("orders-list")



class FoodsListView(ListView):
    model = Food
    template_name = 'food/list.html'
    context_object_name = "foods"



    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        head = self.request.GET.get('head')
        food_id = self.request.GET.get('food_id')

        if search:
            queryset = queryset.filter(
                Q(name__contains = search) | Q(description__contains = search)
            )
        if head:
            queryset = queryset.filter(
                head = head
            )
        if food_id:
            queryset = queryset.filter(
                food_id = food_id
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["foods"] = Food.objects.all()

        context["search"] = self.request.GET.get('search',"")
        food_id = self.request.GET.get('food_id',"")
        if food_id:
            food_id = int(food_id)
        else:
            food_id = 0
        context["food_id"] = food_id

        return context


class FoodsCreateView(CreateView):
    model = Food
    form_class = FoodForm
    success_url = '/foods/list/'
    template_name = 'food/form.html'

class FoodsUpdateView(UpdateView):
    model = Food
    form_class = FoodForm
    success_url = '/foods/list'
    template_name = 'food/form.html'

class FoodsDetailView(DetailView):
    model = Food
    template_name = 'food/detail.html'
    context_object_name = "foods"

def foods_delete(request,pk):
    foods = get_object_or_404(Food,pk=pk)
    foods.delete()
    return redirect("foods-list")





# class OrderListView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request, *args, **kwargs):
#         queryset = Order.objects.all()
#         serializer = OrderSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = OrderSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
# class OrderDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             instance = Order.objects.get(pk=pk)
#             return instance
#         except Order.DoesNotExist as e:
#             raise NotFound(e)
#
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         serializer = OrderSerializer(instance)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         serializer = OrderSerializer(instance=instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
# class FoodListView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request, *args, **kwargs):
#         queryset = Food.objects.all()
#         serializer = FoodSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = FoodSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
# @api_view(["DELETE"])
# def delete_category(request):
#     instance = FoodSerializer.objects.get()
#
# class FoodDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             instance = Food.objects.get(pk=pk)
#             return instance
#         except Food.DoesNotExist as e:
#             raise NotFound(e)
#
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         serializer = FoodSerializer(instance)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         serializer = FoodSerializer(instance=instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

