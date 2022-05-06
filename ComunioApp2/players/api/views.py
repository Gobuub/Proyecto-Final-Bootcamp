
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from players.api.serializer import PlayerSerializer
from players.models import Players


class PlayersApiView(ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer

    '''def list(self, request):
        player_serializer = PlayerSerializer(Players.objects.all(), many=True)

        return Response(data=player_serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk: int):

        player_serializer = PlayerSerializer(Players.objects.get(pk=pk))

        return Response(data=player_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        
        player = PlayerSerializer(data=request.POST)
        player.is_valid(raise_exception=True)
        Players.objects.create(team=player.validated_data['Team'],
                               player=player.validated_data['Player'],
                               continue...)
        
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