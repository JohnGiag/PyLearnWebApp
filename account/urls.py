from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegisterUserView, UserProfileView, ProgressView

urlpatterns = [

    url(r'^register/$', RegisterUserView.as_view(), name='register'),
    url(r'^profile/(?P<pk>[0-9]+)$', UserProfileView.as_view(), name='profile'),
    url(r'^login/$', LoginView.as_view(template_name='account/login.html', redirect_authenticated_user=True),
        name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^progress/(?P<pk>[0-9]+)$', ProgressView.as_view(), name='progress'),

]
