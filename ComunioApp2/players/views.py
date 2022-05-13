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


class AlavesView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Alavés'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class AthleticView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Athletic Club'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class AtleticoView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Atlético Madrid'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class OsasunaView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Osasuna'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class EspanyolView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Espanyol'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class BarcelonaView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Barcelona'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class GetafeView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Getafe'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class GranadaView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Granada'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class RealMadridView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Real Madrid'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class RayoVallecanoView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Rayo Vallecano'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class SevillaView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Sevilla'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class LevanteView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Levante'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class CeltaVigoView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Celta Vigo'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class MallorcaView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Mallorca'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class BetisView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Betis'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class RealSociedadView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Real Sociedad'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class VillarrealView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Villarreal'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class ValenciaView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Valencia'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class ElcheView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Elche'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


class CadizView(View):

    def get(self, request):
        if request.user.is_authenticated:
            context = {
                'players': list(Players.objects.filter(Team='Cádiz'))
            }
            return render(request, 'players.html', context=context)

        return redirect('login')


def upload_image(request):
    if request.method == 'GET':
        return render(request, 'upload_image.html')
