from badges.models import Badge
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import login
from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from account.models import Profile
from .forms import RegisterForm


# Create your views here.
class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = 'home'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        # create user profile
        Profile.objects.create(user=user)
        # login user after registrations
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'],
                            )
        login(self.request, user)
        return super(RegisterUserView, self).form_valid(form)


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'account/profile.html'
    context_object_name = 'profile'

   # def get_context_data(self, **kwargs):
   #     context = super(UserProfileView, self).get_context_data(**kwargs)
   #     # userObject = User.objects.get(id=self.kwargs['pk'])
    #    profileObject = Profile.objects.get(id=self.kwargs['pk'])
    #    completed_quizes = profileObject.getCompletedQuizes(False)
#
    #    completed_exercises = profileObject.getCompletedExercises(False)
    #    context['completed_quizes'] = completed_quizes
     #   context['completed_exercises'] = completed_exercises
    #    return context


class ProgressView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'account/progress.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(ProgressView, self).get_context_data(**kwargs)
        context['badges'] = Badge.objects.exclude(level__iexact="5")
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if int(kwargs['pk']) == request.user.profile.id:
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            return HttpResponseForbidden(render(request, "PermissionDenied.html"))
