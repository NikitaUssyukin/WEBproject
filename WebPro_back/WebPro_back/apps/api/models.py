# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from authentication.models import User


# Create your models here.
#replace with authentication.models.User

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(default='')
    #change UserInfo to User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

    def to_json(self):
        return {
          'id': self.id,
          'title': self.title,
          'body': self.body,
          'user_id': User.to_json(self.user_id),
        }


class Comment(models.Model):
    #add ForeignKey to User
    name = models.CharField(max_length=300)
    comment_body = models.TextField(default='')
    comment_title = models.CharField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author', blank=True, null=True)

    def to_json(self):
        return {
          'id': self.id,
          'name': self.name,
          'comment_body': self.comment_body,
          'comment_title': self.comment_title,
          'post_id': Post.to_json(self.post_id)
        }



class Token(models.Model):
    jwt = models.CharField(max_length=300)
    refreshToken = models.CharField(max_length=300)

    def to_json(self):
        return {
          'id': self.id,
          'jwt': self.jwt,
          'refreshToken': self.refreshToken,
        }
