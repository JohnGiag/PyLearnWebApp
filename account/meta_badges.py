from badges.models import Badge
from badges.utils import MetaBadge

from codingExercise.models import Exercise
from quiz.models import Quiz
from .models import Profile


###Points collecting achievements



class BasePointsCollector(MetaBadge):
    id = "BasePointsCollector"
    title = "Points Collector Base Class"
    description = "This is the Points Collector Base Class.DO NOT CHANGE IT"
    level = "5"

    model = Profile
    one_time_only = True
    target = 1000000

    progress_start = 0
    progress_finish = target

    def get_user(self, instance):
        return instance.user

    def get_progress(self, user):
        progress = self.target if user.profile.points >= self.target else user.profile.points
        return progress

    def check_points(self, instance):
        return instance.user.profile.points >= self.target


class NovicePointsCollector(BasePointsCollector):
    id = "NovicePointsCollector"

    title = "Novice Points Collector"
    description = "Collected 10 points"
    level = "1"
    target = 10


class SeasonedPointsCollector(BasePointsCollector):
    id = "SeasonedPointsCollector"

    title = "Seasoned Points Collector"
    description = "Collected 100 points"
    level = "2"
    target = 100


class AdvancedPointsCollector(BasePointsCollector):
    id = "AdvancedPointsCollector"

    title = "Advanced Points Collector"
    description = "Collected 500 points"
    level = "3"
    target = 500


class MasterPointsCollector(BasePointsCollector):
    id = "MasterPointsCollector"

    title = "Master Points Collector"
    description = "Collected 1000 points"
    level = "4"
    target = 1000


##Completed coding execises achivements


class BaseCompletedExercise(MetaBadge):
    id = "BaseCompletedExercise"
    title = "Completed Exercises Base Class"
    description = "This is theCompleted Exercises  Base Class.DO NOT CHANGE IT"
    level = "5"

    model = Profile
    one_time_only = True
    target = 1000000

    progress_start = 0
    progress_finish = target

    def get_user(self, instance):
        return instance.user

    def get_progress(self, user):
        progress = self.target if user.profile.num_of_copmleted_exercises >= self.target else user.profile.num_of_copmleted_exercises
        return progress

    def check_exercises(self, instance):
        return instance.user.profile.num_of_copmleted_exercises >= self.target


class NoviceCoder(BaseCompletedExercise):
    id = "NoviceCoder"

    title = "Novice Coder"
    description = "Complete 3 coding exercises"
    level = "1"
    target = 3


class SeasonedCoder(BaseCompletedExercise):
    id = "SeasonedCoder"

    title = "Seasoned Coder"
    description = "Complete 10 coding exercises"
    level = "2"
    target = 10


class AdvancedCoder(BaseCompletedExercise):
    id = "AdvancedCoder"

    title = "Advanced Coder"
    description = "Complete 15 coding exercises"
    level = "3"
    target = 15


class MasterCoder(BaseCompletedExercise):
    id = "MasterCoder"

    title = "Master Coder"
    description = "Complete all the coding exercises"
    level = "4"
    target = Exercise.objects.all().count()


##Completed quizes achivements


class BaseCompletedQuiz(MetaBadge):
    id = "BaseCompletedQuiz"
    title = "Completed Quizes Base Class"
    description = "This is theCompleted Quizes  Base Class.DO NOT CHANGE IT"
    level = "5"

    model = Profile
    one_time_only = True
    target = 1000000

    progress_start = 0
    progress_finish = target

    def get_user(self, instance):
        return instance.user

    def get_progress(self, user):
        progress = self.target if user.profile.num_of_copmleted_quizes >= self.target else user.profile.num_of_copmleted_quizes
        return progress

    def check_quizes(self, instance):
        return instance.user.profile.num_of_copmleted_quizes >= self.target


class TriviaNovice(BaseCompletedQuiz):
    id = "TriviaNovice"

    title = "Trivia Novice"
    description = "Complete 1 quiz"
    level = "1"
    target = 1


class TriviaVeteran(BaseCompletedQuiz):
    id = "TriviaVeteran"

    title = "Tivia Veteran"
    description = "Complete 5 quizes"
    level = "2"
    target = 5


class TriviaMaster(BaseCompletedQuiz):
    id = "TriviaMaster"

    title = "Tivia Master"
    description = "Complete 10 quizes"
    level = "3"
    target = 10


class TriviaLegend(BaseCompletedQuiz):
    id = "TriviaLegend"

    title = "Trivia Legend"
    description = "Complete all the quizes"
    level = "4"
    target = Quiz.objects.all().count()


class TriviaHero(MetaBadge):
    id = "TriviaHero"
    title = "Trivia Hero"
    description = "Completed Quizes and have an average score of 75% or higher"
    level = "4"

    model = Profile
    one_time_only = True
    target = 1

    progress_start = 0
    progress_finish = target

    def get_user(self, instance):
        return instance.user

    def get_progress(self, user):
        progress = self.target if user.profile.num_of_copmleted_quizes == Quiz.objects.all().count() and user.profile.quizAvgScore >= 75 else 0
        return progress

    def check_avg_score(self, instance):
        return instance.user.profile.num_of_copmleted_quizes == Quiz.objects.all().count() and instance.user.profile.quizAvgScore >= 75


## acievement hunter achievements
class BaseAchievementHunter(MetaBadge):
    id = "BaseAchievementHunter"
    title = "Achievement Hunter Base Class"
    description = "This is Achievement Hunter  Base Class.DO NOT CHANGE IT"
    level = "5"

    model = Profile
    one_time_only = True
    target = 1000000

    progress_start = 0
    progress_finish = target

    def get_user(self, instance):
        return instance.user

    def get_progress(self, user):
        progress = self.target if user.profile.num_of_achievements >= self.target else user.profile.num_of_achievements
        return progress

    def check_achievements(self, instance):
        return instance.user.profile.num_of_achievements >= self.target


class NoviceAchievementHunter(BaseAchievementHunter):
    id = "NoviceAchievementHunter"

    title = "Novice Achievement Hunter"
    description = "Earn 1 achievement"
    level = "1"
    target = 1


class SeasonedAchievementHunter(BaseAchievementHunter):
    id = "SeasonedAchievementHunter"

    title = "Seasoned Achievement Hunter"
    description = "Earn 5 achievement"
    level = "2"
    target = 5


class AdvancedAchievementHunter(BaseAchievementHunter):
    id = "AdvancedAchievementHunter"

    title = "Advanced Achievement Hunter"
    description = "Earn 10 achievement"
    level = "3"
    target = 10


class MasterAchievementHunter(BaseAchievementHunter):
    id = "MasterAchievementHunter"

    title = "Master Achievement Hunter"
    description = "Earn all the achievements"
    level = "4"
    ###################################################
    # subtract base classes and "phantom achievement" #
    ###################################################
    target = Badge.objects.exclude(level__iexact="5").count()


