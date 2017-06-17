from django.db import models
from datetime import time


class Season(models.Model):
    season_name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()


class Division(models.Model):
    season_id = models.ForeignKey('Season', on_delete=models.CASCADE)
    division_name = models.CharField(max_length=30)


class Team(models.Model):
    team_name = models.CharField(max_length=30)
    division_id = models.ForeignKey('Division', on_delete=models.CASCADE)


class TeamRoster(models.Model):
    team_id = models.ForeignKey('Team', on_delete=models.CASCADE)
    player_id = models.ForeignKey('player.Player', on_delete=models.CASCADE)
    player_number = models.PositiveIntegerField()

    class Meta:
        unique_together = (('team_id', 'player_id'), ('team_id', 'player_number'))


class Game(models.Model):
    division_id = models.ForeignKey('Division', on_delete=models.CASCADE)
    date = models.DateField()
    home = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='game_home')
    away = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='game_away')
    home_goals = models.PositiveIntegerField()  # Inferred
    away_goals = models.PositiveIntegerField()  # Inferred
    winner = models.CharField(max_length=4)
    overtime = models.BooleanField(default=False)
    shootout = models.BooleanField(default=False)
    game_length = models.TimeField()
    first_star = models.ForeignKey('player.Player', related_name='game_first_star')
    second_star = models.ForeignKey('player.Player', related_name='game_second_star')
    third_star = models.ForeignKey('player.Player', related_name='game_third_star')


class PlayerGameStats(models.Model):
    player_id = models.ForeignKey('player.Player', on_delete=models.CASCADE)
    game_id = models.ForeignKey('Game', on_delete=models.CASCADE)
    points = models.PositiveIntegerField()  # Inferred
    goals = models.PositiveIntegerField()  # Inferred
    assists = models.PositiveIntegerField()  # Inferred
    plus_minus = models.IntegerField()  # Inferred
    shots = models.PositiveIntegerField()
    time_on_ice = models.TimeField()
    penalties_in_minutes = models.TimeField()


class Goal(models.Model):
    game_id = models.ForeignKey('Game', on_delete=models.CASCADE)
    goal_scorer = models.ForeignKey('player.Player', related_name='goal_goal_scorer')
    assist_first = models.ForeignKey('player.Player', related_name='goal_assist_first')
    assist_second = models.ForeignKey('player.Player', related_name='goal_assist_second')
    powerplay_goal = models.BooleanField(default=False)
    shorthanded_goal = models.BooleanField(default=False)
    game_winning_goal = models.BooleanField(default=False)
    overtime_goal = models.BooleanField(default=False)