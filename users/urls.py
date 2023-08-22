from django.urls import path
from users.views import UserListView, UserDetailView,TgUserListView,TgUserDetailView

urlpatterns = [
    path('User/', UserListView.as_view(), name='users'),
    path('user/<int:pk>/',UserDetailView.as_view(),name="user-detail"),
    path('tguser/', TgUserListView.as_view(), name='tgusers'),
    path('tguser/<int:pk>/',TgUserDetailView.as_view(),name="tguser-detail"),
]
