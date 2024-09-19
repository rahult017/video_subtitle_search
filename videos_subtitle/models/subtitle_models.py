from django.db import models
from videos_subtitle.models.video_models import Video
from simple_history.models import HistoricalRecords

class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='subtitles')
    language = models.CharField(max_length=10)
    content = models.TextField()
    history = HistoricalRecords()