from django.urls import path
from post.views import PostListView, PostDetailView

urlpatterns = [
    path('post/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
]
