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
from players.views import PlayersView
from users.views import LoginView, LogoutView, IndexView
from django.urls import path, include

import players.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('players/', PlayersView.as_view(), name='players'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('docs/', include_docs_urls(title='Comunio API Docs', public=True)),
    path('api/', include(router.urls)),



]
