from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from category.models import Category
from category.serializers import CategorySerializer
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView
)

from category.forms import CategoryForm
from category.models import Category
from orderfood.models import Food
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AdminPanel(TemplateView):
    template_name = 'index.html'


class MenuPanel(TemplateView):
    template_name = 'menu.html'


class BookPanel(TemplateView):
    template_name = 'book.html'


class AboutPanel(TemplateView):
    template_name = 'about.html'


class IndexView(TemplateView):
    template_name = 'head.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = "category"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        head = self.request.GET.get('head')
        category_id = self.request.GET.get('category_id')

        if search:
            queryset = queryset.filter(
                Q(name__contains=search) | Q(description__contains=search)
            )
        if head:
            queryset = queryset.filter(
                head=head
            )
        if category_id:
            queryset = queryset.filter(
                category_id=category_id
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["category"] = Category.objects.all()

        context["search"] = self.request.GET.get('search', "")
        category_id = self.request.GET.get('category_id', "")
        if category_id:
            category_id = int(category_id)
        else:
            category_id = 0
        context["category_id"] = category_id

        return context


class HomePanel(ListView):
    model = Food
    template_name = 'head.html'
    context_object_name = "foods"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')

        if search:
            queryset = queryset.filter(
                Q(name__contains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get("search", "")
        return context


class CategorysCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = '/category/list/'
    template_name = 'category/form.html'


class CategorysUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = '/category/list'
    template_name = 'category/form.html'


class CategorysDetailView(DetailView):
    model = Category
    template_name = 'category/detail.html'
    context_object_name = "category"


def categorys_delete(request, pk):
    categorys = get_object_or_404(Category, pk=pk)
    categorys.delete()
    return redirect("category-list")

# class CategoryListView(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request, *args, **kwargs):
#         queryset = Category.objects.all()
#         serializer = CategorySerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#
#
# class CategoryDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             instance = Category.objects.get(pk=pk)
#             return instance
#         except Category.DoesNotExist as e:
#             raise NotFound(e)
#
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         serializer = CategorySerializer(instance)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         serializer = CategorySerializer(instance=instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object(pk=kwargs.get("pk"))
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
