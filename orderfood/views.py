from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from orderfood.models import Order,Food
from orderfood.serializers import OrderSerializer,FoodSerializer
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view

class OrderListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

class OrderDetailView(APIView):
    def get_object(self, pk):
        try:
            instance = Order.objects.get(pk=pk)
            return instance
        except Order.DoesNotExist as e:
            raise NotFound(e)

    def get(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = OrderSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = OrderSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class FoodListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        queryset = Food.objects.all()
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = FoodSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
def delete_category(request):
    instance = FoodSerializer.objects.get()

class FoodDetailView(APIView):
    def get_object(self, pk):
        try:
            instance = Food.objects.get(pk=pk)
            return instance
        except Food.DoesNotExist as e:
            raise NotFound(e)

    def get(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = FoodSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = FoodSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

