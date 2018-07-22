from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MatchDetails
# Create your views here.


@login_required
def CricketCenterIndexView(request):
    return render(request, "cricket_center/cricket_center_index.html",)


@login_required
def SingleMatchView(request, slug):
    match = MatchDetails.objects.filter(match_url=slug)
    print(match[0].team_one, match[0].team_two)
    return render(request, "cricket_center/match.html",)
