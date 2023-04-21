from rest_framework.routers import DefaultRouter
from videos.api.views import VideoApiViewSet

router_videos = DefaultRouter()

router_videos.register(prefix='videos', basename='videos', viewset=VideoApiViewSet)