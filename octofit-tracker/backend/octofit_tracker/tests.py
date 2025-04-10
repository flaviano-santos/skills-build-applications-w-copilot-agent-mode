from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        user1 = User.objects.create(username="user1", email="user1@example.com", password="password123")
        user2 = User.objects.create(username="user2", email="user2@example.com", password="password123")
        team = Team.objects.create(name="Team Test")
        team.members.set([user1, user2])
        self.assertEqual(team.name, "Team Test")
        self.assertEqual(team.members.count(), 2)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        activity = Activity.objects.create(user=user, activity_type="Running", duration=timedelta(minutes=30))
        self.assertEqual(activity.activity_type, "Running")
        self.assertEqual(activity.duration, timedelta(minutes=30))

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard_entry(self):
        user = User.objects.create(username="testuser", email="test@example.com", password="password123")
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Morning Run", description="A quick 5km run to start the day.")
        self.assertEqual(workout.name, "Morning Run")
        self.assertEqual(workout.description, "A quick 5km run to start the day.")
