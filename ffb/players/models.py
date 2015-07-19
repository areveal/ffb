from django.db import models


class Player(models.Model):
    nflgame_id = models.CharField(max_length=50, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    college = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True, default=0)
    weight = models.IntegerField(null=True, blank=True, default=0)
    position = models.CharField(max_length=50, null=True, blank=True)
    team = models.CharField(max_length=4, null=True, blank=True)
