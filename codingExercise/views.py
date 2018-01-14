from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseNotFound

from account.models import Profile, CompletedExercise
from .forms import ExerciseForm, ExerciseAdminForm
from .models import Exercise
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView,DetailView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy


# Create your views here.



class CodingExerciseListView(LoginRequiredMixin,ListView):

    model = Exercise
    template_name = 'codingExercise/exercise_list.html'

    def get_context_data(self, **kwargs):
        context = super(CodingExerciseListView, self).get_context_data(**kwargs)
        #userObject = User.objects.get(username=self.request.user)
        profileObject = Profile.objects.get(user__username=self.request.user)
        completed_exercises = profileObject.getCompletedExercises(True)

        context['completed_exercises'] = completed_exercises
        return context

class CodingExerciseDetailView(LoginRequiredMixin,DetailView):
    model = Exercise
    context_object_name = 'ex'
    template_name = 'codingExercise/exercise.html'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return HttpResponseNotFound(render(request,"NotFound.html"))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, *args, **kwargs):

        current_exercise = Exercise.objects.filter(id=str(self.kwargs['pk']))
        # get quiz name
        for exercise in current_exercise.values('name'):
            current_exercise_name = exercise['name']

        profileObject = Profile.objects.get(user__username=self.request.user)
        previous_score_query = CompletedExercise.objects.filter(userProfile=profileObject, exercise_name=current_exercise_name)
        if previous_score_query.count() == 0:
            userProfile = Profile.objects.get(user__username=self.request.user)
            userProfile.points += 5
            userProfile.num_of_copmleted_exercises += 1
            completed_exercise = CompletedExercise(userProfile=userProfile, exercise_name=current_exercise_name)
            userProfile.save()
            completed_exercise.save()

        next_pk=int(kwargs['pk'])+1
        if next_pk <= int(Exercise.objects.all().count()):
            return HttpResponseRedirect(str(next_pk))
        else:
            return redirect('codingExercise:finished')


    def get_context_data(self, **kwargs):
        context = super(CodingExerciseDetailView, self).get_context_data(**kwargs)
        #if self.request.method == 'POST':
          #  form = ExerciseForm(self.request.POST)
       # else:
        form = ExerciseForm()
        form2 = ExerciseAdminForm(self.request.POST)
        context['form'] = form
        context['form2'] = form2
        context['active'] = 'ce'
        return context



class Finished(LoginRequiredMixin,TemplateView):

    template_name = 'codingExercise/finished.html'

