from django.db import models
from users.models import User

class Video(models.Model):
    url = models.URLField(max_length=600)
    description = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __init__(self):
        return self.url