from django.conf.urls import url
from django.views.generic import TemplateView

from .views import CodingExerciseListView, CodingExerciseDetailView,Finished
from django.conf.urls import handler404

app_name = 'codingExercise'
urlpatterns = [
    #url(r'^/(?P<pk>\d+)/$', CodingExerciseDetailView.as_view(), name='exercise'),
    url(r'^finished$',Finished.as_view(), name='finished'),
    url(r'^$', CodingExerciseListView.as_view(), name='exercise_list'),
    url(r'^(?P<pk>[0-9]+)$',CodingExerciseDetailView.as_view(), name='exercise'),


]

