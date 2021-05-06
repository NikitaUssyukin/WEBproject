
from django.urls import path
from .views.views_cbv import CommentsListAPIView, CommentsDetailAPIView
from .views.views_fbv import post_list, post_write, post_detail

app_name = 'api'
urlpatterns = [
    path('comments/', CommentsListAPIView.as_view()),
    path('comments/<int:pk>/', CommentsDetailAPIView.as_view()),

    path('posts/', post_list),
    path('posts/write/', post_write),
    path('posts/<int:post_id>/', post_detail)
]