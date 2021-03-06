from badges.models import Badge
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import login
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from account.models import Profile, CompletedExercise
from .forms import RegisterForm



class RegisterUserView(CreateView):
    """RegisterUserView is a view used to show the registration form"""
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
    """ UserProfileView is a view used to show a users profile"""
    model = Profile
    template_name = 'account/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        profileObject = Profile.objects.get(user__username=self.request.user)
        completed_exercises = CompletedExercise.objects.filter(userProfile=profileObject).values_list('exercise_name',
                                                                                                      flat=True).distinct()
        context['completed_exercises'] = completed_exercises
        return context


class ProgressView(LoginRequiredMixin, DetailView):
    """ ProgressView is a view used to show a users progress page"""
    model = Profile
    template_name = 'account/progress.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(ProgressView, self).get_context_data(**kwargs)
        context['badges'] = Badge.objects.exclude(level__iexact="5")
        return context

    def get(self, request, *args, **kwargs):
        """
        Function to handle GET requests at /account/progress
        A user is allowed to only view his personal Progress page.
        """
        self.object = self.get_object()
        if int(kwargs['pk']) == request.user.profile.id:
            context = self.get_context_data()
            return self.render_to_response(context)
        else:
            return HttpResponseForbidden(render(request, "PermissionDenied.html"))
