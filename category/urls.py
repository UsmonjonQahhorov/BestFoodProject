from django.urls import path
from category import views


urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("category/list/",views.CategoryListView.as_view(),name="category-list"),
    path("category/create/",views.CategorysCreateView.as_view(),name="category-create"),
    path("category/<int:pk>/update/",views.CategorysUpdateView.as_view(),name="category-update"),
    path("category/<int:pk>/detail/",views.CategorysDetailView.as_view(),name="category-detail"),
    path("category/<int:pk>/delete/",views.categorys_delete,name="category-delete"),
]




# urlpatterns = [
#     path('category/', CategoryListView.as_view(), name='categorys'),
#     path('category/<int:pk>/',CategoryDetailView.as_view(),name="category-detail"),
# ]


