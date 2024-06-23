from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('chatrooms/',views.chat_rooms,name='chatrooms'),
    path('newroom/', views.newroom, name="newroom"),
    path('newroom/register_room',views.register_room,name='register_room'),
    path('<str:room>/', views.room, name="room"),
]

# video min 8:24:49