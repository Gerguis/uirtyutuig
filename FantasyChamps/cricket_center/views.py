from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MatchDetail, IndiaPakistanTeam
import time
from .forms import CreateTeamKeeperForm, CreateTeamBatsmenForm, CreateTeamAllroundersForm, CreateTeamBowlersForm
from django.http import HttpResponseRedirect, HttpResponse
from django import forms


@login_required
def CricketCenterIndexView(request):
    match_obj = MatchDetail.objects.filter(match_tick__gte=time.time()).order_by('match_date')
    return render(request, "cricket_center/cricket_center_index.html", context={'match_obj': match_obj})


@login_required
def SingleMatchView(request, slug):
    return render(request, "cricket_center/match.html",)


def CreateTeamView(request, slug):
    team_created = False
    keeper_form = CreateTeamKeeperForm()
    batsmen_form = CreateTeamBatsmenForm()
    allrounders_form = CreateTeamAllroundersForm()
    bowlers_form = CreateTeamBowlersForm()
    if request.method == 'POST':
        keeper_form = CreateTeamKeeperForm(data=request.POST)
        batsmen_form = CreateTeamBatsmenForm(data=request.POST)
        allrounders_form = CreateTeamAllroundersForm(data=request.POST)
        bowlers_form = CreateTeamBowlersForm(data=request.POST)
        if keeper_form.is_valid() and batsmen_form.is_valid() and allrounders_form.is_valid() and bowlers_form.is_valid():
            user_teams_obj = IndiaPakistanTeam.objects.filter(username_of_player__exact=request.user.username)
            if user_teams_obj.count() < 3:
                new_team_no = user_teams_obj.count() + 1
                for obj in user_teams_obj:
                    if obj.team_no == new_team_no:
                        new_team_no = new_team_no + 1
            else:
                return HttpResponse("Maximum reched out")
            Keeper_Dict = list(keeper_form.cleaned_data.keys())[list(keeper_form.cleaned_data.values()).index(True)]
            Selected_Keeper = {'Player': Keeper_Dict, 'Team': '', 'Captain': False, 'Vice_Captain': False, 'Current_Points': 0, 'Total_Points': 0}
            Selected_Batsmen = [k for k, v in batsmen_form.cleaned_data.items() if v is True]
            Selected_Allrounders = [k for k, v in allrounders_form.cleaned_data.items() if v is True]
            Selected_Bowlers = [k for k, v in bowlers_form.cleaned_data.items() if v is True]
            list_of_players = []
            list_of_players = [str(Selected_Keeper)] + list_of_players
            for Batsman in Selected_Batsmen:
                list_of_players.append(str({'Player': Batsman, 'Team': '', 'Captain': False, 'Vice_Captain': False, 'Current_Points': 0, 'Total_Points': 0}))

            for Allrounder in Selected_Allrounders:
                list_of_players.append(str({'Player': Allrounder, 'Team': '', 'Captain': False, 'Vice_Captain': False, 'Current_Points': 0, 'Total_Points': 0}))

            for Bowler in Selected_Bowlers:
                list_of_players.append(str({'Player': Bowler, 'Team': '', 'Captain': False, 'Vice_Captain': False, 'Current_Points': 0, 'Total_Points': 0}))

            if len(list_of_players) != 11:
                try:
                    raise forms.ValidationError('Please Select only 11 Players')
                except forms.ValidationError as e:
                    bowlers_form.add_error(None, e)
                    return render(request, 'cricket_center/create_team.html', {'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created})

            team_obj = IndiaPakistanTeam(
                                            team_no=new_team_no,
                                            username_of_player=request.user.username,
                                            match_slug=slug,
                                            Keeper=list_of_players[0],
                                            Player2=list_of_players[1],
                                            Player3=list_of_players[2],
                                            Player4=list_of_players[3],
                                            Player5=list_of_players[4],
                                            Player6=list_of_players[5],
                                            Player7=list_of_players[6],
                                            Player8=list_of_players[7],
                                            Player9=list_of_players[8],
                                            Player10=list_of_players[9],
                                            Player11=list_of_players[10],
                                        )
            team_obj.save()
            team_created = True
            return HttpResponseRedirect('/cricket_center/match' + '/' + slug)

    return render(request, 'cricket_center/create_team.html', {'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created})

# def CreateTeamView(request, slug):
#     print("Fiifrst Come First")
#     keeper_form = CreateTeamKeeperForm(request.POST)
#     print("after call first")
#     # team_created = False
#     # if keeper_form.is_valid():
#     #     print("form is valid")
#     #     # team_obj = IndiaPakistanTeam(Keeper=request.POST.get('Dinesh_Ramdin'))
#     #     # team_obj.save()
#     #     print(keeper_form.cleaned_data)
#     #     team_created = True
#     team_created = False
#     keeper_form = CreateTeamKeeperForm(request.POST or None)
#     print(keeper_form.is_valid())
#     if keeper_form.is_valid():
#         print("Form is validated")
#         print(keeper_form.cleaned_data)
#         team_created = True

#     return render(request, 'cricket_center/create_team.html', {'keeper_form': keeper_form, 'team_created': team_created})
