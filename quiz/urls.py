from django.conf.urls import url
from .views import QuizView, QuizListView


app_name = 'quiz'
urlpatterns = [
    url(r'^$', QuizListView.as_view(), name='quiz_list'),
    url(r'^(?P<pk>[0-9]+)$', QuizView.as_view(), name='quiz_details'),

]
