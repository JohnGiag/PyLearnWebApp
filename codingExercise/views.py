from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView

from account.models import Profile, CompletedExercise
from .forms import ExerciseForm
from .models import Exercise, Chapter


# Create your views here.



class CodingExerciseListView(LoginRequiredMixin, ListView):
    model = Chapter
    template_name = 'codingExercise/exercise_list.html'

    def get_context_data(self, **kwargs):
        context = super(CodingExerciseListView, self).get_context_data(**kwargs)
        # userObject = User.objects.get(username=self.request.user)
        profileObject = Profile.objects.get(user__username=self.request.user)
        completed_exercises = profileObject.getCompletedExercises(True)
        context['completed_exercises'] = completed_exercises
        return context


class CodingExerciseDetailView(LoginRequiredMixin, DetailView):
    model = Exercise
    context_object_name = 'ex'
    template_name = 'codingExercise/exercise.html'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return HttpResponseNotFound(render(request, "NotFound.html"))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, *args, **kwargs):

        current_exercise = Exercise.objects.filter(id=str(self.kwargs['pk']))
        # get exercise name
        current_exercise_name = current_exercise.values('name')[0]['name']
        form = ExerciseForm(self.request.POST)
        if form.is_valid():
            # print(form.cleaned_data['text'])
            answer = "".join(('<pre class="python"><br>', form.cleaned_data['text'], '<br></pre>'))
            userProfile = Profile.objects.get(user__username=self.request.user)
            # check if new solution was used
            completed_exercise, created = CompletedExercise.objects.get_or_create(userProfile=userProfile,
                                                                                  exercise_name=current_exercise_name,
                                                                                  answer=answer)
            if created:
                userProfile.points += 5
                userProfile.num_of_copmleted_exercises += 1
                completed_exercise.save()
                userProfile.save()

        next_pk = int(kwargs['pk']) + 1
        if next_pk <= int(Exercise.objects.all().count()):
            return HttpResponseRedirect(str(next_pk))
        else:
            return redirect('codingExercise:finished')

    def get_context_data(self, **kwargs):
        context = super(CodingExerciseDetailView, self).get_context_data(**kwargs)
        form = ExerciseForm()
        context['form'] = form
        return context



        # if self.request.method == 'POST':
        #  form = ExerciseForm(self.request.POST)
        # else:

        ###################################################################################
        # profileObject = Profile.objects.get(user__username=self.request.user)
        ###################################################################################
        #
        # context['active'] = 'ce'


class Finished(LoginRequiredMixin, TemplateView):
    template_name = 'codingExercise/finished.html'
