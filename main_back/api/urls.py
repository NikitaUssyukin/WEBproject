from django.urls import path
from .views.views_cbv import CommentsListAPIView, CommentsDetailAPIView
from .views.views_fbv import post_list, post_detail

app_name = 'api'
urlpatterns = [
    path('comments/', CommentsListAPIView.as_view()),
    #path('comments/<int:comment_id>/', CommentsDetailAPIView.as_view()),
]