from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from account.models import Profile, CompletedQuiz
from codingExercise.models import Chapter
from .models import Quiz


# Create your views here.


class QuizListView(LoginRequiredMixin, ListView):
    model = Chapter
    template_name = 'quiz/quiz_list.html'

    def get_context_data(self, **kwargs):
        context = super(QuizListView, self).get_context_data(**kwargs)
        profile_object = Profile.objects.get(user__username=self.request.user)
        completed_quizes = profile_object.getCompletedQuizes(True)
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

        # get quiz name
        current_quiz = Quiz.objects.filter(id=str(self.kwargs['pk']))
        current_quiz_name = current_quiz.values('name')[0]['name']

        qn = 1
        correct = {}  # dict with {QuestionName : correct answer} pairs
        for question_text, correct_answer in zip(current_quiz.values('question__question_text'),
                                                 current_quiz.values('question__correct_answer')):
            correct.update({question_text['question__question_text']: correct_answer['question__correct_answer']})
            qn += 1

        userAnswers = {}
        correct_count = 0

        for i in self.request.POST:
            # print(i)

            if i.startswith('Q'):
                # print(i)
                #
                if str(self.request.POST[i]) == correct[i]:
                    correct_count += 1  # count correct answers
                userAnswers.update({i: self.request.POST[i]})
        correct_percentage = float(correct_count / (qn - 1))
        correct_percentage = float("{0:.1f}".format(correct_percentage * 100))

        # check if quiz completed previously

        profileObject = Profile.objects.get(user__username=self.request.user)

        completed_quiz, created = CompletedQuiz.objects.get_or_create(userProfile=profileObject,
                                                                      quiz_name=current_quiz_name)
        print(completed_quiz)
        if created:
            completed_quiz.save()
            # first attempt
            first_attempt = True
            previous_attempt_score = 0
            newHighscore = False
            # save new attempt

            profileObject.num_of_copmleted_quizes += 1
            profileObject.setAvgQuizSore(correct_percentage)
            profileObject.points += correct_percentage

            completed_quiz.score = str(correct_percentage)
            profileObject.save()
            completed_quiz.save()
        else:
            previous_attempt_score = completed_quiz.score
            newHighscore = False
            if correct_percentage > float(previous_attempt_score):  # replace when new score is better
                newHighscore = True
                completed_quiz.score = str(correct_percentage)
                completed_quiz.save()

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
