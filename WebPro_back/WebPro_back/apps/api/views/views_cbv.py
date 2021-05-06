from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.serializers import CommentsSerializer, UserSerializer, PostSerializer
from api.models import Comment, Post
from authentication.models import User

from django.contrib.auth.mixins import LoginRequiredMixin

class CommentsListAPIView( APIView):
    def get(self, request):
        comments = Comment.objects.order_by('-id')
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        post = Post.objects.get(id=request.data.get('post'))
        user = User.objects.get(id=request.data.get('user'))
        print(request.data)
        _comment = request.data
        _comment['user'] = user
        _comment['post'] = post
        
        Comment.objects.create(
            post=post, user=user,
            name = request.data.get('name'),
            comment_body = request.data.get('comment_body'),
            comment_title = request.data.get('comment_title'),    
        )
        return Response({ 'message': 'created' })


class CommentsDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(id=pk)
        except Comment.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        comment = self.get_object(pk)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk=None):
        comment = self.get_object(pk)
        comment.comment_body = request.data.get('comment_body')
        comment.comment_title = request.data.get('comment_title')
        comment.save()
        return Response({ 'message': 'updated' })

    def delete(self, request, pk=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response({'message': 'deleted'}, status=204)



class UserInfoListAPIView(APIView):
    def get(self, request):
        users = UserInfo.objects.order_by('-id')
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
