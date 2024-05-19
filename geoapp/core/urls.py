from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index" ),
    path('chat/', views.chatbot, name="chatbot"),
    path('chat/<chat_id>',views.chat, name="chat"),
    path('getResponse', views.getResponse, name="getResponse"),
    path("map/", views.map, name = "map"),
]