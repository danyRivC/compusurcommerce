from django.urls import path
from comments.views import create_comment

app_name='comments'
urlpatterns=[
    path("createdcomment", create_comment, name="createcomment")
]