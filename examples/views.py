from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from codingExercise.models import Chapter
from examples.models import Example


class ExampleListView(LoginRequiredMixin, ListView):
    """ ExampleListView is a view used to show a list of all Examples separated in chapters """
    model = Chapter
    template_name = 'examples/examples_list.html'


class ExampleDetailView(LoginRequiredMixin, DetailView):
    """ExampleDetailView is a view used to show a specific Example"""
    model = Example
    template_name = 'examples/example.html'
    context_object_name = 'example'

    def post(self, *args, **kwargs):
        next_pk = int(kwargs['pk']) + 1
        # if example with id next_pk exists redirect to it else try the next id
        if next_pk <= int(Example.objects.latest("id").id):
            while Example.objects.filter(id=next_pk).count() == 0:
                next_pk += 1
            else:
                return HttpResponseRedirect(str(next_pk))
        else:
            return redirect('codingExercise:finished')
