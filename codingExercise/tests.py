from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from .views import CodingExerciseListView,CodingExerciseDetailView,Finished
from .models import Exercise
from account.models import Profile,CompletedExercise

# Create your tests here.

class CodingExerciseViewsTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testUser', email='test@user.com', password='top_secret')
        self.profile = Profile.objects.create(user=self.user)
        self.testEx2 = Exercise.objects.create(name="testEx2", instructions="test inst", test="test test")
        self.testEx = Exercise.objects.create(name="testEx", instructions="test inst", test="test test",
                                              next=self.testEx2)
        CompletedExercise.objects.create(userProfile=self.profile,exercise_name=self.testEx.name)


    def test_list_view_not_loged_in(self):
        request = self.factory.get('/ce/')
        request.user = AnonymousUser()
        response = CodingExerciseListView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_detail_view_not_loged_in(self):
        request = self.factory.get('/ce/')
        request.user = AnonymousUser()
        response = CodingExerciseDetailView.as_view()(request,pk=self.testEx.id)
        self.assertEqual(response.status_code, 302)

    def test_list_view_loged_in(self):
        request = self.factory.get('/ce/')
        request.user = self.user

        response = CodingExerciseListView.as_view()(request)
        self.assertEqual(response.status_code, 200)


    def test_detail_view_loged_in_exercise_exists(self):
        request = self.factory.get('/ce/')
        request.user = self.user

        #exercise that exists
        response = CodingExerciseDetailView.as_view()(request,pk=self.testEx.id)
        self.assertEqual(response.status_code, 200)

    def test_detail_view_loged_in_exercise_does_not_exist(self):
        request = self.factory.get('/ce/')
        request.user = self.user


        # exercise that doesn't exist
        response = CodingExerciseDetailView.as_view()(request, pk=322145)
        self.assertEqual(response.status_code, 404)


    def test_finished_view_not_loged_in(self):
        request = self.factory.get('/finished/')
        request.user = AnonymousUser()
        response = Finished.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_finished_view_loged_in(self):
        request = self.factory.get('/finished/')
        request.user = self.user


        response = Finished.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_completed_already_completed_exercise(self):
        request = self.factory.post('/ce/',{id:self.testEx.id})
        request.user = self.user
        # exercise that exists
        response = CodingExerciseDetailView.as_view()(request, pk=self.testEx.id)
        self.assertEqual(CompletedExercise.objects.filter(userProfile=self.profile).count(), 1)

    def test_completed_new_exercise(self):
        request = self.factory.post('/ce/',{id:self.testEx2.id})
        request.user = self.user
        # exercise that exists
        response = CodingExerciseDetailView.as_view()(request, pk=self.testEx2.id)
        self.assertEqual(CompletedExercise.objects.filter(userProfile=self.profile).count(), 2)



