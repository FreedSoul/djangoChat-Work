from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chat',views.chat_rooms,name='chatrooms')
]