from rest_framework.decorators import api_view
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse

from rest_framework.request import Request
from rest_framework.response import Response
from api.models import Comment, Post
from api.serializers import UserSerializer, PostSerializer, CommentsSerializer, UserWithPostsSerializer

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.order_by('-id')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#post_id instead of user_id
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = UserSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'message': 'deleted'}, status=204)

