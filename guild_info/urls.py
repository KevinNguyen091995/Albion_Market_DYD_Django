from django.urls import path

from .views import PlayerSearchInfo, Top5MemberInfo

urlpatterns = [
    path('api/guildinfo/playersearch/<str:player_name>', PlayerSearchInfo.as_view(), name='player_search'),
    path('api/guildinfo/top5', Top5MemberInfo.as_view()),
]
