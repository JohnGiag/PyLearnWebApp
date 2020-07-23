from django.conf.urls import url
from .views import LeaderboardListView


app_name = 'leaderboard'
urlpatterns = [
    url(r'^$', LeaderboardListView.as_view(), name='leaderboard_list'),

]
