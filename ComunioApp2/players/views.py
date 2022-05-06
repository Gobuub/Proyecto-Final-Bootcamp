import requests.utils
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from players.models import Players
from ComunioApp2.resources import PlayerResource


class PlayersView(View):

    def get(self, request):
        if request.user.is_authenticated:

            context = {
                'players': list(Players.objects.all())
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class TeamView(View):

    def get(self, request, team: 'string'):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(team=team))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')
