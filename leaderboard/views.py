from django.shortcuts import render
from django.views.generic import ListView
from account.models import Profile



class LeaderboardListView(ListView):
    """
    LeaderboardListView is a view to show the leaderboard list of all the users
    """
    model = Profile
    template_name = 'leaderBoard/leaderboard_list.html'
    paginate_by = 25

    def get_queryset(self):
        queryset = Profile.objects.all().order_by('-points')
        return queryset
