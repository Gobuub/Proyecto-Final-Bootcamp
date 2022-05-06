from rest_framework.routers import DefaultRouter

from players.api.views import PlayersApiView

router = DefaultRouter()

router.register(prefix='players', basename='players', viewset=PlayersApiView)
