from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User, TgUser
from users.serializers import UserSerializer, TgUserSerializer
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view


class UserListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    def get_object(self, pk):
        try:
            instance = User.objects.get(pk=pk)
            return instance
        except User.DoesNotExist as e:
            raise NotFound(e)

    def get(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = UserSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = UserSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TgUserListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = TgUser.objects.all()
        serializer = TgUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TgUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class TgUserDetailView(APIView):
    def get_object(self, pk):
        try:
            instance = TgUser.objects.get(pk=pk)
            return instance
        except TgUser.DoesNotExist as e:
            raise NotFound(e)

    def get(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = TgUserSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = TgUserSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
