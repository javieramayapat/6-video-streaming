from rest_framework.viewsets import ModelViewSet
from videos.models import Video

class VideoApiViewSet(ModelViewSet):
    # serializer to return informaiton
    queryset = Video.objects.all()