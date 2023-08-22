from django.urls import path
from category.views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name='categorys'),
    path('category/<int:pk>/',CategoryDetailView.as_view(),name="category-detail"),
]
