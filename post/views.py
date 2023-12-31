from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from category.models import Category
from post.models import Post
from post.serializers import PostSerializer
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view


class PostListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
def delete_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(["DELETE"])
# def delete_category(request):
#     instance = PostSerializer.objects.get()
#     instance.delete()
#     return instance

class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            instance = Post.objects.get(pk=pk)
            return instance
        except Post.DoesNotExist as e:
            raise NotFound(e)

    def get(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = PostSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        serializer = PostSerializer(instance=instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(pk=kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        instance = Post.objects.all()
        serializer = PostSerializer(instance, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class PostDetailView(APIView):

    def get_objects(self, pk):
        try:
            instance = Post.objects.get(pk=pk)
            return instance
        except Post.DoesNotExist as e:
            raise NotFound(e)

    def get(self, request, *args, **kwargs):
        instance = self.get_objects(pk=kwargs.get("pk"))
        serializer = PostSerializer(instance)
        return Response(data=serializer.data, status=status.HTTP_200_OK)  # Response qaytarishni qo'shing

    def put(self, request, *args, **kwargs):
        instance = self.get_objects(pk=kwargs.get("pk"))
        serializer = PostSerializer(instance, data=request.data, partial=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        instance = self.get_objects(pk=kwargs.get("pk"))
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
