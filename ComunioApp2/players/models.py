

from django.db import models
# Create your models here.
from django.template.defaultfilters import default


class Players(models.Model):
    id = models.IntegerField(primary_key=True)
    Team = models.CharField(max_length=50)
    Player = models.CharField(max_length=50)
    Position = models.CharField(max_length=50)
    On_start = models.IntegerField()
    Points_Average = models.IntegerField()
    Last_5_games_points = models.CharField(max_length=100)
    J_4 = models.IntegerField()
    J_3 = models.IntegerField()
    J_2 = models.IntegerField()
    J_1 = models.IntegerField()
    J_Actual = models.IntegerField()
    Avg_last_5_games = models.IntegerField()
    Value = models.IntegerField()
    Squad_Average_Points = models.IntegerField()
    J_4_Squad_Points = models.IntegerField()
    J_3_Squad_Points = models.IntegerField()
    J_2_Squad_Points = models.IntegerField()
    J_1_Squad_Points = models.IntegerField()
    J_Actual_Squad_Points = models.IntegerField()
    Squad_Avg_last_5_Games = models.IntegerField()
    Value_Squad = models.IntegerField()
    vs = models.CharField(max_length=50)
    Vs_Team = models.CharField(max_length=50)
    Vs_Squad_Average_Points = models.IntegerField()
    J_4_Vs_Squad_Points = models.IntegerField()
    J_3_Vs_Squad_Points = models.IntegerField()
    J_2_Vs_Squad_Points = models.IntegerField()
    J_1_Vs_Squad_Points = models.IntegerField()
    J_Actual_Vs_Squad_Points = models.IntegerField()
    Vs_Squad_Avg_last_5_Games = models.IntegerField()
    Vs_Value_Squad = models.IntegerField()
    Team_clas = models.IntegerField()
    Vs_Team_clas = models.IntegerField()

    def __str__(self):
        return self.Player


class Image(models.Model):
    image = models.ImageField(upload_to= 'img', default='players/static/img/no-img.png')
    team = models.CharField(max_length=100)
