from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'character', views.CharacterViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
