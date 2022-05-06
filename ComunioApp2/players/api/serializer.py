from rest_framework import serializers

from players.models import Players


class PlayerSerializer(serializers.ModelSerializer):
    '''
   Team = serializers.CharField(max_length=50)
    Player = serializers.CharField(max_length=50)
    Position = serializers.CharField(max_length=50)
    On_start = serializers.IntegerField()
    Points_Average = serializers.IntegerField()
    Last_5_games_points = serializers.CharField(max_length=100)
    J_4 = serializers.IntegerField()
    J_3 = serializers.IntegerField()
    J_2 = serializers.IntegerField()
    J_1 = serializers.IntegerField()
    J_Actual = serializers.IntegerField()
    Avg_last_5_games = serializers.IntegerField()
    Value = serializers.IntegerField()
    Squad_Average_Points = serializers.IntegerField()
    J_4_Squad_Points = serializers.IntegerField()
    J_3_Squad_Points = serializers.IntegerField()
    J_2_Squad_Points = serializers.IntegerField()
    J_1_Squad_Points = serializers.IntegerField()
    J_Actual_Squad_Points = serializers.IntegerField()
    Squad_Avg_last_5_Games = serializers.IntegerField()
    Value_Squad = serializers.IntegerField()
    vs = serializers.CharField(max_length=50)
    Vs_Team = serializers.CharField(max_length=50)
    Vs_Squad_Average_Points = serializers.IntegerField()
    J_4_Vs_Squad_Points = serializers.IntegerField()
    J_3_Vs_Squad_Points = serializers.IntegerField()
    J_2_Vs_Squad_Points = serializers.IntegerField()
    J_1_Vs_Squad_Points = serializers.IntegerField()
    J_Actual_Vs_Squad_Points = serializers.IntegerField()
    Vs_Squad_Avg_last_5_Games = serializers.IntegerField()
    Vs_Value_Squad = serializers.IntegerField()
    Team_clas = serializers.IntegerField()
    Vs_Team_clas = serializers.IntegerField()'''

    class Meta:
        model = Players
        fields = '__all__'
