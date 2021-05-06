from rest_framework import serializers
from api.models import Comment, Post
from authentication.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)



class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    body = serializers.CharField()
    
    #
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'user')


class CommentsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    comment_body = serializers.CharField()
    comment_title = serializers.CharField()
    post = PostSerializer()
    user = UserSerializer()

    def create(self, validated_data):
        comment_body = Comment.objects.create(name=validated_data.get('comment_body'))
        return comment_body

    def update(self, instance, validated_data):
        instance.comment_body = validated_data.get('comment_body', instance.name)
        instance.save()
        return instance




class UserWithPostsSerializer(serializers.ModelSerializer):
    body = PostSerializer(many=True, read_only=True)


class Meta:
    model = PostSerializer
    fields = ('id', 'title', 'body', 'user_id')
