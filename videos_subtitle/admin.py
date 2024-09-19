from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from videos_subtitle.models import video_models,subtitle_models

admin.site.register(video_models.Video, SimpleHistoryAdmin)
admin.site.register(subtitle_models.Subtitle, SimpleHistoryAdmin)