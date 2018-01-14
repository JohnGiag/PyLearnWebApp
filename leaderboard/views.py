from django.shortcuts import render
from django.views.generic import ListView
from account.models import Profile

# Create your views here.


class LeaderboardListView(ListView):
    model = Profile
    template_name = 'leaderBoard/leaderboard_list.html'
    paginate_by = 25



    def get_queryset(self):
        queryset=Profile.objects.all(). order_by('-points')
        return  queryset
