"""ComunioApp2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.documentation import include, include_docs_urls

from players.api.router import router
from players.api.views import PlayersApiView
from players.views import PlayersView, AlavesView, AthleticView, AtleticoView, OsasunaView, EspanyolView, BarcelonaView, \
    GetafeView, GranadaView, RealMadridView, RayoVallecanoView, SevillaView, LevanteView, CeltaVigoView, MallorcaView, \
    BetisView, RealSociedadView, VillarrealView, ValenciaView, ElcheView, CadizView
from users.views import LoginView, LogoutView, IndexView
from django.urls import path, include

import players.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('players/', PlayersView.as_view(), name='players'),
    path('athletic/', AthleticView.as_view(), name='athletic'),
    path('alaves/', AlavesView.as_view(), name='alaves'),
    path('atletico/', AtleticoView.as_view(), name='atletico'),
    path('espanyol/', EspanyolView.as_view(), name='espanyol'),
    path('barcelona/', BarcelonaView.as_view(), name='barcelona'),
    path('getafe/', GetafeView.as_view(), name='getafe'),
    path('granada/', GranadaView.as_view(), name='granada'),
    path('realmadrid/', RealMadridView.as_view(), name='realmadrid'),
    path('rayovallecano/', RayoVallecanoView.as_view(), name='rayo'),
    path('sevilla/', SevillaView.as_view(), name='sevilla'),
    path('levante/', LevanteView.as_view(), name='levante'),
    path('celtavigo/', CeltaVigoView.as_view(), name='celta'),
    path('mallorca/', MallorcaView.as_view(), name='mallorca'),
    path('betis/', BetisView.as_view(), name='betis'),
    path('realsociedad/', RealSociedadView.as_view(), name='realsociedad'),
    path('villarreal/', VillarrealView.as_view(), name='villarreal'),
    path('valencia/', ValenciaView.as_view(), name='valencia'),
    path('elche/', ElcheView.as_view(), name='elche'),
    path('cadiz/', CadizView.as_view(), name='cadiz'),
    path('osasuna/', OsasunaView.as_view(), name='osasuna'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('docs/', include_docs_urls(title='Comunio API Docs', public=True)),
    path('api/', include(router.urls)),



]

