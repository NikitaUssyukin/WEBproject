# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user_name = models.CharField(max_length=300)
    description = models.TextField(default='')

    def to_json(self):
        return {
          'id': self.id,
          'user_name': self.user_name,
          'description': self.description,
        }


class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField(default='')
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='posts')

    def to_json(self):
        return {
          'id': self.id,
          'title': self.title,
          'body': self.body,
          'user_id': UserInfo.to_json(self.user_id),
        }


class Comment(models.Model):
    name = models.CharField(max_length=300)
    comment_body = models.TextField(default='')
    comment_title = models.CharField(max_length=300)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def to_json(self):
        return {
          'id': self.id,
          'name': self.name,
          'comment_body': self.comment_body,
          'comment_title': self.comment_title,
          'post_id': Post.to_json(self.post_id)
        }


class User(models.Model):
    name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

    def to_json(self):
        return {
          'id': self.id,
          'name': self.name,
          'password': self.password,
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
