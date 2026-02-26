"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

import os

@api_view(['GET'])
def api_root(request):
    """Return root API links using the codespace hostname if available.

    The workspace provides a CODESPACE_NAME environment variable when
    running in GitHub Codespaces.  Constructing the base URL from this
    variable ensures the responses reference the public HTTPS endpoint
    (https://$CODESPACE_NAME-8000.app.github.dev) and avoids any
    certificate warnings that might arise from using request.get_host().
    If the variable is not set (e.g. running locally), fall back to the
    request's own host information.
    """
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        base = f"https://{codespace}-8000.app.github.dev/api"
    else:
        # build_absolute_uri will include scheme and host from the
        # incoming request; strip any trailing slash since we append
        # components manually below.
        base = request.build_absolute_uri('/api').rstrip('/')

    return Response({
        'users': f"{base}/users/",
        'teams': f"{base}/teams/",
        'activities': f"{base}/activities/",
        'leaderboard': f"{base}/leaderboard/",
        'workouts': f"{base}/workouts/",
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('', include(router.urls)),
]
