from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet


router = SimpleRouter()

router.register('posts', PostViewSet)

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
