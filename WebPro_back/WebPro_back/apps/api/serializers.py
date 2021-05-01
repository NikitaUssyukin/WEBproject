from rest_framework import serializers
from api.models import UserInfo, Comment, Post


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)


class CommentsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(write_only=True)
    comment_body = serializers.CharField(write_only=True)
    comment_title = serializers.CharField(read_only=True)
    post_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        comment_body = CommentsSerializer.objects.create(name=validated_data.get('comment_body'))
        return comment_body

    def update(self, instance, validated_data):
        instance.comment_body = validated_data.get('comment_body', instance.name)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    id = UserSerializer(read_only=True)
    title = serializers.CharField(write_only=True)
    body = serializers.CharField(read_only=True)
    #
    user_id = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'user_id')


class UserWithPostsSerializer(serializers.ModelSerializer):
    body = PostSerializer(many=True, read_only=True)


class Meta:
    model = PostSerializer
    fields = ('id', 'title', 'body', 'user_id')
