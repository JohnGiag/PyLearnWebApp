from django.conf.urls import url

from examples.views import ExampleListView, ExampleDetailView

app_name = 'examples'
urlpatterns = [
   url(r'^$', ExampleListView.as_view(), name='examples_list'),
   url(r'^(?P<pk>[0-9]+)$', ExampleDetailView.as_view(), name='example'),

]
