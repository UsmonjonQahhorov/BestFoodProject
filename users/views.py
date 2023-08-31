from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.models import User, TgUser
from users.serializers import UserSerializer, TgUserSerializer, SmsVerificationSerializer
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view, action

from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView
)
from users.forms import UserForm, TgUserForm
from users.models import User, TgUser
from rest_framework.viewsets import ModelViewSet
from users.serializers import TgUserSerializer


class TgUserViewSet(ModelViewSet):
    queryset = TgUser.objects.all()
    serializer_class = TgUserSerializer

    def get_serializer_class(self):
        if self.action == "verify":
            return SmsVerificationSerializer
        return self.serializer_class

    @action(detail=False, methods=["POST"])
    def verify(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        chat_id = serializer.data.get("chat_id")
        code = serializer.data.get("code")
        tu = TgUser.objects.get(chat_id=chat_id)
        if tu.sms == code:
            tu.is_verified = True
            tu.save()
            return Response(status=200)
        return Response(status=400)


class IndexView(TemplateView):
    template_name = 'index.html'


class UsersListView(ListView):
    model = User
    template_name = 'user/list.html'
    context_object_name = "users"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        role = self.request.GET.get('role')
        user_id = self.request.GET.get('user_id')

        if search:
            queryset = queryset.filter(
                Q(name__contains=search) | Q(description__contains=search)
            )
        if role:
            queryset = queryset.filter(
                role=role
            )
        if user_id:
            queryset = queryset.filter(
                user_id=user_id
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search"] = self.request.GET.get('search', "")
        user_id = self.request.GET.get('user_id', "")
        if user_id:
            user_id = int(user_id)
        else:
            user_id = 0
        context["user_id"] = user_id

        return context


class UsersCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = '/users/list/'
    template_name = 'user/form.html'


class UsersUpdateView(UpdateView):
    model = User
    form_class = UserForm
    success_url = '/users/list/'
    template_name = 'user/form.html'


class UsersDetailView(DetailView):
    model = User
    template_name = 'user/detail.html'
    context_object_name = "users"


def users_delete(request, pk):
    users = get_object_or_404(User, pk=pk)
    users.delete()
    return redirect("users-list")


# ======================================TgUser==================================


class TgUsersListView(ListView):
    model = TgUser
    template_name = 'tgusers/list.html'
    context_object_name = "tgusers"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        role = self.request.GET.get('role')
        tgusers_id = self.request.GET.get('tgusers_id')

        if search:
            queryset = queryset.filter(
                Q(name__contains=search) | Q(description__contains=search)
            )
        if role:
            queryset = queryset.filter(
                role=role
            )
        if tgusers_id:
            queryset = queryset.filter(
                tgusers_id=tgusers_id
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search"] = self.request.GET.get('search', "")
        chat_id = self.request.GET.get('chat_id', "")  # tgusers_id
        if chat_id:
            chat_id = int(chat_id)
        else:
            chat_id = 0
        context["chat_id"] = chat_id

        return context


class TgUsersCreateView(CreateView):
    model = TgUser
    form_class = TgUserForm
    success_url = '/tgusers/list/'
    template_name = 'tgusers/form.html'


class TgUsersUpdateView(UpdateView):
    model = TgUser
    form_class = TgUserForm
    success_url = '/tgusers/list'
    template_name = 'tgusers/form.html'


class TgUsersDetailView(DetailView):
    model = TgUser
    template_name = 'tgusers/detail.html'
    context_object_name = "tgusers"


def tgusers_delete(request, pk):
    tgusers = get_object_or_404(TgUser, pk=pk)
    tgusers.delete()
    return redirect("tgusers-list")

#
# class UserListView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#
# class UserDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             instance = User.objects.get(pk=pk)
#             return instance
#         except User.DoesNotExist as e:
#             raise NotFound(e)
#
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         serializer = UserSerializer(instance)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         serializer = UserSerializer(instance=instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class TgUserListView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         queryset = TgUser.objects.all()
#         serializer = TgUserSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = TgUserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#
# class TgUserDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             instance = TgUser.objects.get(pk=pk)
#             return instance
#         except TgUser.DoesNotExist as e:
#             raise NotFound(e)
#
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         serializer = TgUserSerializer(instance)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         serializer = TgUserSerializer(instance=instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
