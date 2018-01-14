from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from account.models import Profile, CompletedQuiz
from .models import Quiz, Question
from .views import QuizListView, QuizView


# Create your tests here.

class QuizViewsTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testUser', email='test@user.com', password='top_secret')
        self.profile = Profile.objects.create(user=self.user)
        self.question = Question.objects.create(question_text='test question', answer1='1', answer2='2', answer3='3',
                                                correct_answer='1')
        self.testQuiz = Quiz.objects.create(name="testQuiz")
        self.testQuiz2 = Quiz.objects.create(name="testQuiz2")
        self.negativeQuiz = Quiz.objects.create(name="negativeQuiz")
        self.testQuiz.questions.add(self.question)
        self.testQuiz2.questions.add(self.question)
        self.negativeQuiz.questions.add(self.question)
        self.firstAttempt = CompletedQuiz.objects.create(userProfile=self.profile, quiz_name=self.testQuiz.name,
                                                         score="10")
        self.negativeAttempt = CompletedQuiz.objects.create(userProfile=self.profile, quiz_name=self.negativeQuiz.name,
                                                         score="-1")

    def test_list_view_not_loged_in(self):
        request = self.factory.get('/quiz/')
        request.user = AnonymousUser()
        response = QuizListView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_list_view_loged_in(self):
        request = self.factory.get('/quiz/')
        request.user = self.user

        response = QuizListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_detail_view_not_loged_in(self):
        request = self.factory.get('/quiz/')
        request.user = AnonymousUser()
        response = QuizView.as_view()(request, pk=self.testQuiz.id)
        self.assertEqual(response.status_code, 302)

    def test_detail_view_loged_in_quiz_exists(self):
        request = self.factory.get('/quiz/')
        request.user = self.user

        # exercise that exists
        response = QuizView.as_view()(request, pk=self.testQuiz.id)
        self.assertEqual(response.status_code, 200)
        # exercise that doesn't exist
        response = QuizView.as_view()(request, pk=345421)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_loged_in_quiz_does_not_exist(self):
        request = self.factory.get('/quiz/')
        request.user = self.user

        response = QuizView.as_view()(request, pk=345421)
        self.assertEqual(response.status_code, 404)

    def completed_already_completed_quiz_with_worse_score(self):
        request = self.factory.post('/ce/', {id: self.testQuiz.id})
        request.user = self.user
        # exercise that exists
        response = QuizView.as_view()(request, pk=self.testQuiz.id)
        self.assertContains(response,'which is not an improvement over your previous score')
        self.assertEqual(CompletedQuiz.objects.filter(userProfile=self.profile).count(), 2)

    def completed_already_completed_quiz_with_better_score(self):

        request = self.factory.post('/ce/', {id: self.negativeQuiz.id})
        request.user = self.user
        # exercise that exists
        response = QuizView.as_view()(request, pk=self.negativeQuiz.id)
        self.assertContains(response,'which is an improvement')
        self.assertEqual(CompletedQuiz.objects.filter(userProfile=self.profile).count(), 2)

    def completed_new_quiz(self):
        request = self.factory.post('/ce/', {id: self.testQuiz2.id})
        request.user = self.user
        # exercise that exists
        response = QuizView.as_view()(request, pk=self.testQuiz2.id)
        self.assertEqual(CompletedQuiz.objects.filter(userProfile=self.profile).count(), 3)


    def test_quiz_completion_cases(self):
        self.completed_already_completed_quiz_with_worse_score()
        self.completed_already_completed_quiz_with_better_score()
        self.completed_new_quiz()

