from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from account.models import Profile, CompletedQuiz
from .models import Quiz


# Create your views here.


class QuizListView(LoginRequiredMixin, ListView):
    model = Quiz
    template_name = 'quiz/quiz_list.html'
    context_object_name = 'quiz_list'

    def get_context_data(self, **kwargs):
        context = super(QuizListView, self).get_context_data(**kwargs)
        profileObject = Profile.objects.get(user__username=self.request.user)
        completed_quizes = profileObject.getCompletedQuizes(True)
        context['active'] = 'quiz'
        context['completed_quizes'] = completed_quizes
        return context


class QuizView(LoginRequiredMixin, DetailView):
    model = Quiz
    context_object_name = 'quiz'

    template_name = 'quiz/quiz.html'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return HttpResponseNotFound(render(request, "NotFound.html"))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, *args, **kwargs):
        first_attempt = False

        current_quiz = Quiz.objects.filter(id=str(self.kwargs['pk']))
        # get quiz name
        for quiz in current_quiz.values('name'):
            current_quiz_name = quiz['name']

        qn = 1
        correct = {}  # dict with {QuestionName : correct answer} pairs
        for question in current_quiz.values('questions__correct_answer'):
            correct.update({"".join(("q", str(qn))): question['questions__correct_answer']})
            qn += 1

        userAnswers = {}
        correct_count = 0
        for i in self.request.POST:
            if 'q' in i:

                if str(self.request.POST[i]) == correct[i]:
                    correct_count += 1  # count correct answers
                userAnswers.update({i: self.request.POST[i]})
        correct_percentage = float(correct_count / (qn - 1))
        correct_percentage = float("{0:.1f}".format(correct_percentage * 100))

        # check if quiz completed previously

        profileObject = Profile.objects.get(user__username=self.request.user)
        previous_score_query = CompletedQuiz.objects.filter(userProfile=profileObject, quiz_name=current_quiz_name)
        if previous_score_query.count() != 0:
            previous_attempt = CompletedQuiz.objects.get(userProfile=profileObject, quiz_name=current_quiz_name)
            previous_attempt_score = previous_attempt.score
            newHighscore = False
            if correct_percentage > float(previous_attempt.score):  # replace when new score is better
                newHighscore = True
                # delete previous attempt
                previous_attempt.delete()
                # save new attempt

                quiz_score = CompletedQuiz(userProfile=profileObject, quiz_name=current_quiz_name,
                                           score=str(correct_percentage))
                profileObject.save()
                quiz_score.save()
        else:  # first attempt
            first_attempt = True
            previous_attempt_score = 0
            newHighscore = False
            # save new attempt
            profileObject.num_of_copmleted_quizes += 1
            profileObject.setAvgQuizSore(correct_percentage)
            profileObject.points += correct_percentage

            quiz_score = CompletedQuiz(userProfile=profileObject, quiz_name=current_quiz_name,
                                       score=str(correct_percentage))
            profileObject.save()
            quiz_score.save()

        # user.completed_quizes.add(quiz_score)

        context = {
            'quiz': current_quiz,
            'correct': correct.items(),
            'correct_percentage': correct_percentage,
            'userAnswers': userAnswers.items(),
            'newHighsScore': newHighscore,
            'prevScore': previous_attempt_score,
            'first_attempt': first_attempt,

        }

        # show results
        return render(self.request, 'quiz/results.html', context)
