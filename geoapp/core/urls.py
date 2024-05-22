from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'locations', views.LocationViewSet)

urlpatterns = [
    path('',views.index, name="index" ),
    path('chat/', views.chatbot, name="chatbot"),
    path('chat/<chat_id>',views.chat, name="chat"),
    path('getResponse', views.getResponse, name="getResponse"),
    path("map/", views.map, name = "map"),
    path('api/', include(router.urls)),
    path('api/search/', views.search_locations, name='search_locations'),
]