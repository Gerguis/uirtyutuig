from django.db import models
# Create your models here.


class MatchDetails(models.Model):
    macth_name = models.CharField(max_length=100)
    match_date = models.DateTimeField()
    match_url = models.CharField(max_length=25)
    team_one = models.CharField(max_length=25, default='Team A')
    team_two = models.CharField(max_length=25, default='Team B')

    def __str__(self):
        return self.macth_name
