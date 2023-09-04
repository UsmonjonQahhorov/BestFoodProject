from django.urls import path
from category import views
from rest_framework.routers import DefaultRouter

from category.views import CategoryViewSet

router = DefaultRouter()
router.register("category_list", CategoryViewSet, basename="category_getlist")

urlpatterns = [
                  path("", views.IndexView.as_view(), name="index"),
                  path("category/list/", views.CategoryListView.as_view(), name="category-list"),
                  path("category/create/", views.CategorysCreateView.as_view(), name="category-create"),
                  path("category/<int:pk>/update/", views.CategorysUpdateView.as_view(), name="category-update"),
                  path("category/<int:pk>/detail/", views.CategorysDetailView.as_view(), name="category-detail"),
                  path("category/<int:pk>/delete/", views.categorys_delete, name="category-delete"),
              ] + router.urls

# urlpatterns = [
#     path('category/', CategoryListView.as_view(), name='categorys'),
#     path('category/<int:pk>/',CategoryDetailView.as_view(),name="category-detail"),
# ]
