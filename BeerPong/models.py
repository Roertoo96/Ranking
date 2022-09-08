from pyexpat import model
from django.db import models
from datetime import date

# Create your models here.


class BeerPongRankingTable(models.Model):
    rank = models.IntegerField(default=0, null=False)
    username = models.CharField(max_length=30, default='', null=False)
    wins = models.IntegerField(default=0, null=False)
    games = models.IntegerField(default=0, null=False)
    created_at = models.DateField(default=date.today)