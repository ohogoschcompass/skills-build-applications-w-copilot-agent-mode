from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Limpar dados existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Criar times
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Criar usuários
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        # Criar atividades
        Activity.objects.create(user='Spider-Man', type='Running', duration=30)
        Activity.objects.create(user='Iron Man', type='Cycling', duration=45)
        Activity.objects.create(user='Wonder Woman', type='Swimming', duration=25)
        Activity.objects.create(user='Batman', type='Walking', duration=60)

        # Criar leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=85)

        # Criar workouts
        Workout.objects.create(name='Hero HIIT', description='Treino intenso para super-heróis.')
        Workout.objects.create(name='Power Yoga', description='Yoga para força e flexibilidade.')

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
