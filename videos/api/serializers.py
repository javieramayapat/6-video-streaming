from rest_framework import serializers
from videos.models import Video

class VideoSerializer(serializers.Serializer):
    class Meta:
        model = Video
        fields = ('id', 'description', 'url')