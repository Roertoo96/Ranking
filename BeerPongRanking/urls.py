"""BeerPongRanking URL Configuration

"""
from django.contrib import admin
from django.urls import path
from BeerPong.views import home, ranking
from BeerPong.views import login
from BeerPong.views import BeerPongRank
from BeerPong.views import ranking
from BeerPong.views import addmatch
from BeerPong.views import adduser




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('login/', login),
    path('BeerPong/', BeerPongRank),
    path('ranking/', ranking),
    path('addmatch', addmatch),
    path('adduser', adduser),

]
