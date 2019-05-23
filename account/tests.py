from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory
from django.test import TestCase

from account.views import RegisterUserView, UserProfileView, ProgressView
from .models import Profile, CompletedQuiz


# Create your tests here.


class QuizMethodTest(TestCase):
    def setUp(self):
        self.p = Profile.objects.create(user=User.objects.create(username="quizUser"), num_of_copmleted_quizes=2)
        CompletedQuiz.objects.create(userProfile=self.p, quiz_name="quiz1", score="10")
        CompletedQuiz.objects.create(userProfile=self.p, quiz_name="quiz2", score="10")

    def test_get_completed_quizes_flat(self):
        self.assertEqual(str(self.p.getCompletedQuizes(True)), "<QuerySet ['quiz1', 'quiz2']>")

    def test_get_completed_quizes_non_flat(self):
        self.assertEqual(str(self.p.getCompletedQuizes(False)),
                         '<QuerySet [<CompletedQuiz: quiz1>, <CompletedQuiz: quiz2>]>')

    def test_setAvgQuizScore(self):
        self.assertEqual(self.p.quizAvgScore, 0)
        self.assertEqual(self.p.num_of_copmleted_quizes, 2)
      #  self.p.setAvgQuizSore(100)
        self.p.save()
        self.assertEqual(self.p.quizAvgScore, 50)


class AccountViewsTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testUser', email='test@user.com', password='top_secret')
        self.otherUser = User.objects.create_user(username='testUser2', email='test2@user.com', password='top_secret')
        self.myProfile = Profile.objects.create(user=self.user)
        self.otherProfile = Profile.objects.create(user=self.otherUser)

    def test_registration_view_not_loged_in(self):
        request = self.factory.get('/register/')
        request.user = AnonymousUser()
        response = RegisterUserView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_registration_view__loged_in(self):
        request = self.factory.get('/register/')
        request.user = self.user
        response = RegisterUserView.as_view()(request)
        self.assertEqual(response.status_code, 403)

    def test_profile_view_not_loged_in(self):
        request = self.factory.get('/profile/')
        request.user = AnonymousUser()
        response = UserProfileView.as_view()(request, pk=self.otherProfile.id)
        self.assertEqual(response.status_code, 302)

    def test_my_profile(self):
        request = self.factory.get('/profile/')
        request.user = self.user
        response = UserProfileView.as_view()(request, pk=self.myProfile.id)
        self.assertContains(response, "My profile")

    def test_other_user_profile(self):
        request = self.factory.get('/profile/')
        request.user = self.user
        response = UserProfileView.as_view()(request, pk=self.otherUser.id)
        self.assertContains(response, self.otherUser.username)

    def test_other_user_profile2(self):
        request = self.factory.get('/profile/')
        request.user = self.user
        response = UserProfileView.as_view()(request, pk=self.otherUser.id)
        self.assertFalse(response.__contains__('My Profile'))


class ProgressViewsTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testUser', email='test@user.com', password='top_secret')
        self.otherUser = User.objects.create_user(username='testUser2', email='test2@user.com', password='top_secret')
        self.myProfile = Profile.objects.create(user=self.user)
        self.otherProfile = Profile.objects.create(user=self.otherUser)

    def test_progress_view_not_loged_in(self):
        request = self.factory.get('/progress/')
        request.user = AnonymousUser()
        response = ProgressView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_progress_view_loged_in(self):
        request = self.factory.get('/progress/')
        request.user = self.user
        response = ProgressView.as_view()(request, pk=self.myProfile.id)
        self.assertEqual(response.status_code, 200)

    def test_other_progress_view_not_loged_in(self):
        request = self.factory.get('/progress/')
        request.user = AnonymousUser()
        response = ProgressView.as_view()(request, pk=self.otherProfile.id)
        self.assertEqual(response.status_code, 302)

    def test_other_progress_view_loged_in(self):
        request = self.factory.get('/progress/')
        request.user = self.user
        response = ProgressView.as_view()(request, pk=self.otherProfile.id)
        self.assertEqual(response.status_code, 403)
