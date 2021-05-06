from rest_framework.decorators import api_view
from django.http.request import HttpRequest

from django.http.response import HttpResponse, JsonResponse

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from api.models import Comment, Post
from api.serializers import UserSerializer, PostSerializer, CommentsSerializer, UserWithPostsSerializer

from authentication.models import User

@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@permission_classes(IsAuthenticated)
@api_view(['POST'])
def post_write(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.data.get("user_id"))
        Post.objects.create(
            user=user,
            title=request.data.get("title"),
            body=request.data.get("body")
        )
        return Response({ "message": "Entity created successfully." })



#post_id instead of user_id
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        post.title = request.data.get('title')
        post.body = request.data.get('body')
        post.save()
        return Response({ 'message': 'edited' })
    elif request.method == 'DELETE':
        post.delete()
        return Response({'message': 'deleted'}, status=204)

