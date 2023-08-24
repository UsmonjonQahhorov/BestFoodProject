from django.urls import path
from users import views


urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("users/list/",views.UsersListView.as_view(),name="users-list"),
    path("users/create/",views.UsersCreateView.as_view(),name="users-create"),
    path("users/<int:pk>/detail/",views.UsersDetailView.as_view(),name="users-detail"),
    path("users/<int:pk>/update/",views.UsersUpdateView.as_view(),name="users-update"),
    path("users/<int:pk>/delete/",views.users_delete, name="users-delete"),
    path("tgusers/list/",views.TgUsersListView.as_view(),name="tgusers-list"),
    path("tgusers/create/",views.TgUsersCreateView.as_view(),name="tgusers-create"),
    path("tgusers/<int:pk>/detail/",views.TgUsersDetailView.as_view(),name="tgusers-detail"),
    path("tgusers/<int:pk>/update/",views.TgUsersUpdateView.as_view(),name="tgusers-update"),
    path("tgusers/<int:pk>/delete/",views.tgusers_delete, name="tgusers-delete"),
]




# urlpatterns = [
#     path('User/', UserListView.as_view(), name='users'),
#     path('user/<int:pk>/',UserDetailView.as_view(),name="user-detail"),
#     path('tgusers/', TgUserListView.as_view(), name='tgusers'),
#     path('tgusers/<int:pk>/',TgUserDetailView.as_view(),name="tgusers-detail"),
# ]
