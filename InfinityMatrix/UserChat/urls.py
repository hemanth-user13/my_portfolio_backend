from django.urls import path
from .views import *

urlpatterns = [
    path('chat', UserChat.as_view(), name='user-chat-api'),


]
