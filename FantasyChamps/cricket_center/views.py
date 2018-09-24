from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import MatchDetail, IndiaWestIndiesTeam, PlayerDetail, JoiningDetail, ContestDetail
import time
from .forms import CreateTeamKeeperForm, CreateTeamBatsmenForm, CreateTeamAllroundersForm, CreateTeamBowlersForm
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.db.models import Q
from django.http import JsonResponse
from accounts.models import Profile
from django.http import Http404


@login_required(login_url='IndexView')
def CricketCenterIndexView(request):
    match_obj = MatchDetail.objects.filter(match_tick__gte=time.time()).order_by('match_date')
    return render(request, "cricket_center/cricket_center_index.html", context={'match_obj': match_obj})


@login_required(login_url='IndexView')
def SingleMatchView(request, slug):
    print(slug)
    try:
        match_obj = MatchDetail.objects.get(match_slug__exact=slug)
    except MatchDetail.DoesNotExist:
        return HttpResponse("Something went Wrong!")
    all_contests_obj = match_obj.contestdetail_set.all()
    print(all_contests_obj)
    total_teams = IndiaWestIndiesTeam.objects.filter(username_of_player__exact=request.user.username)
    return render(request, "cricket_center/match.html", context={'all_contests_obj': all_contests_obj, 'match_slug': slug, 'total_teams': total_teams})


@login_required(login_url='IndexView')
def PayAndJoin(request):
    error = False
    log_in_error = False
    contest_error = False
    match_slug = request.POST.get('match_slug')
    contest_slug = request.POST.get('contest_slug')
    all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug)

    try:
        user = Profile.objects.get(user__username__exact=request.user.username)
    except Profile.DoesNotExist:
        error = True
        log_in_error = True

    try:
        contest = ContestDetail.objects.get(contest_slug__exact=contest_slug)
    except ContestDetail.DoesNotExist:
        error = True
        contest_error = True

    if error is False:
        user = Profile.objects.get(user__username__exact=request.user.username)
        all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug)
        contest = ContestDetail.objects.get(contest_slug__exact=contest_slug)
        user_balance = user.balance
        user_bonus = user.bonus
        joined_players = all_joined.count()
        contest_name = contest.contest_name
        contest_price = contest.contest_price
        contest_fee = contest.contest_fee
        low_balance = 0
        add_money = 0
        if contest.bonus_contest is True:
            if user_bonus >= 10:
                deduction_from_bonus = 10
                new_bonus = user_bonus - deduction_from_bonus
                user.bonus = new_bonus
                deduction_from_main = contest_fee - deduction_from_bonus
                if deduction_from_main > user_balance:
                    low_balance = 1
                    add_money = deduction_from_main - user_balance
                else:
                    print(user_balance, deduction_from_main)
                    new_balance = user_balance - deduction_from_main
                    user.balance = new_balance
                    join_obj = JoiningDetail(joined_user=request.user.username, joined_contest_slug=contest_slug, joined_user_team=1, match_slug=match_slug)
                    user.save()
                    join_obj.save()
                    contest.save()

            else:
                deduction_from_bonus = user_bonus
                deduction_from_main = contest_fee - deduction_from_bonus
                user.bonus = user_bonus - deduction_from_bonus
                deduction_from_main = contest_fee - deduction_from_bonus
                if deduction_from_main > user_balance:
                    low_balance = 1
                    add_money = deduction_from_main - user_balance
                else:
                    user.balance = user_balance - deduction_from_main
                    join_obj = JoiningDetail(joined_user=request.user.username, joined_contest_slug=contest_slug, joined_user_team=1, match_slug=match_slug)
                    user.save()
                    join_obj.save()
                    contest.save()
        else:
            deduction_from_bonus = 0
            deduction_from_main = contest_fee
            if deduction_from_main > user_balance:
                low_balance = 1
                add_money = deduction_from_main - user_balance
            else:
                user.balance = user_balance - deduction_from_main
                join_obj = JoiningDetail(joined_user=request.user.username, joined_contest_slug=contest_slug, joined_user_team=1, match_slug=match_slug)
                user.save()
                join_obj.save()
                contest.save()
        print(user, user.balance, user.bonus, joined_players, contest_name, contest_price, contest_fee, deduction_from_bonus, deduction_from_main, low_balance, add_money)
        data = {
            'called': "Ok I Got A Call From AJAX to Views",
            'contest_name': contest_name,
            'user_balance': user_balance,
            'user_bonus': user_bonus,
            'joined_players': joined_players,
            'contest_price': contest_price,
            'contest_fee': contest_fee,
            'deduction_from_bonus': deduction_from_bonus,
            'deduction_from_main': deduction_from_main,
            'low_balance': low_balance,
            'add_money': add_money,
            'match_slug': match_slug,
            'contest_slug': contest_slug,
            'balance': user.balance,
            'bonus': user.bonus,
            'error': error,
        }
        return JsonResponse(data)
    else:
        data = {
            "error": error,
            "log_in_error": log_in_error,
            "contest_error": contest_error,
        }
        return JsonResponse(data)


@login_required(login_url='IndexView')
def ProceedToPay(reques):
    print("Ok I am Wokruinf Fine")
    return HttpResponse("Invalid login details supplied.")


@login_required(login_url='IndexView')
def ContestJoinNow(request, match_slug, contest_slug):
    print(request)
    error = False
    log_in_error = False
    contest_error = False
    match_slug = match_slug
    contest_slug = contest_slug
    all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug)

    try:
        user = Profile.objects.get(user__username__exact=request.user.username)
    except Profile.DoesNotExist:
        error = True
        log_in_error = True

    try:
        contest = ContestDetail.objects.get(contest_slug__exact=contest_slug)
    except ContestDetail.DoesNotExist:
        error = True
        contest_error = True

    if error is False:
        user = Profile.objects.get(user__username__exact=request.user.username)
        all_joined = JoiningDetail.objects.filter(joined_contest_slug__exact=contest_slug)
        contest = ContestDetail.objects.get(contest_slug__exact=contest_slug)
        user_bonus = user.bonus
        user_balance = user.balance
        joined_players = all_joined.count()
        contest_name = contest.contest_name
        contest_price = contest.contest_price
        contest_fee = contest.contest_fee
        low_balance = 0
        add_money = 0
        if contest.bonus_contest is True:
            if user_bonus >= 10:
                deduction_from_bonus = 10
                bonus_balance_after_deduction = user_bonus - deduction_from_bonus
                deduction_from_main = contest_fee - deduction_from_bonus
                if deduction_from_main > user_balance:
                    low_balance = 1
                    add_money = deduction_from_main - user_balance
                    main_balance_after_deduction = 0
                else:
                    main_balance_after_deduction = user_balance - deduction_from_main
            else:
                deduction_from_bonus = user_bonus
                deduction_from_main = contest_fee - deduction_from_bonus
                bonus_balance_after_deduction = user_bonus - deduction_from_bonus
                deduction_from_main = contest_fee - deduction_from_bonus
                if deduction_from_main > user_balance:
                    low_balance = 1
                    add_money = deduction_from_main - user_balance
                    main_balance_after_deduction = 0
                else:
                    main_balance_after_deduction = user_balance - deduction_from_main
        else:
            deduction_from_bonus = 0
            bonus_balance_after_deduction = user_bonus
            deduction_from_main = contest_fee
            if deduction_from_main > user_balance:
                low_balance = 1
                add_money = deduction_from_main - user_balance
                main_balance_after_deduction = 0
            else:
                main_balance_after_deduction = user_balance - deduction_from_main

        print(user, user_balance, joined_players, contest_name, contest_price, contest_fee, deduction_from_bonus, deduction_from_main, bonus_balance_after_deduction, main_balance_after_deduction, low_balance, add_money)
        data = {
            'called': "Ok I Got A Call From AJAX to Views",
            'contest_name': contest_name,
            'user_balance': user_balance,
            'user_bonus': user_bonus,
            'joined_players': joined_players,
            'contest_price': contest_price,
            'contest_fee': contest_fee,
            'deduction_from_bonus': deduction_from_bonus,
            'deduction_from_main': deduction_from_main,
            'bonus_balance_after_deduction': bonus_balance_after_deduction,
            'main_balance_after_deduction': main_balance_after_deduction,
            'low_balance': low_balance,
            'add_money': add_money,
            'match_slug': match_slug,
            'contest_slug': contest_slug,
            'error': error,
        }
        return JsonResponse(data)

    else:
        data = {
            "error": error,
            "log_in_error": log_in_error,
            "contest_error": contest_error,
        }
        return JsonResponse(data)


@login_required(login_url='IndexView')
def CreateTeamView(request, slug):
    players_obj = PlayerDetail.objects.filter(Q(player_current_team__exact='WI') | Q(player_current_team__exact='IND'))
    # player_points_obj = PlayerDetail.objects.filter(match_slug__exact=slug)
    # players_points = player_points_obj[0]
    # # players_points = {}
    # for player in player_points_obj[0]:
    #     players_points[player]=player.
    team_created = False
    user_teams_obj = None
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
            print(request.POST.get("captain"))
            print(request.POST.get("vice"))
            user_teams_obj = IndiaWestIndiesTeam.objects.filter(username_of_player__exact=request.user.username)
            if user_teams_obj.count() < 3:
                new_team_no = user_teams_obj.count() + 1
                for obj in user_teams_obj:
                    if obj.team_no == new_team_no:
                        new_team_no = new_team_no + 1
            else:
                return HttpResponse("Maximum reched out")
            Keeper_Dict = list(keeper_form.cleaned_data.keys())[list(keeper_form.cleaned_data.values()).index(True)]
            Selected_Keeper = Keeper_Dict
            Selected_Batsmen = [k for k, v in batsmen_form.cleaned_data.items() if v is True]
            Selected_Allrounders = [k for k, v in allrounders_form.cleaned_data.items() if v is True]
            Selected_Bowlers = [k for k, v in bowlers_form.cleaned_data.items() if v is True]
            list_of_players = []
            list_of_players = [str(Selected_Keeper)] + list_of_players
            for Batsman in Selected_Batsmen:
                list_of_players.append(str(Batsman))

            for Allrounder in Selected_Allrounders:
                list_of_players.append(str(Allrounder))

            for Bowler in Selected_Bowlers:
                list_of_players.append(str(Bowler))

            # total_sallery = 0
            # for player in list_of_players:
            #     print(type(player))
            #     players_sallery_obj = IndiaWestIndiesTeam.objects.filter(username_of_player__exact=player)
            #     print(players_sallery_obj)
            #     # total_sallery = total_sallery + players_sallery_obj.player_credit_points

            # print(total_sallery)
            print(list_of_players)

            if len(list_of_players) != 11:
                try:
                    raise forms.ValidationError('Please Select only 11 Players')
                except forms.ValidationError as e:
                    keeper_form.add_error(None, e)
                    return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created})

            if request.POST.get("captain") is None or request.POST.get("captain") not in list_of_players or request.POST.get("captain") is "off":
                try:

                    raise forms.ValidationError('Please Select your Captain')
                except forms.ValidationError as e:
                    keeper_form.add_error(None, e)
                    return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created})

            if request.POST.get("vice") is None or request.POST.get("vice") not in list_of_players or request.POST.get("captain") is "off":
                try:
                    raise forms.ValidationError('Please Select your Vice Captain')
                except forms.ValidationError as e:
                    keeper_form.add_error(None, e)
                    return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created})
            print(request.POST.get("captain"))
            team_obj = IndiaWestIndiesTeam(
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
                                            Captain=request.POST.get("captain"),
                                            Vice_Captain=request.POST.get("vice"),
                                        )
            team_obj.save()
            team_created = True
            return HttpResponseRedirect('/cricket_center/match' + '/' + slug)
    return render(request, 'cricket_center/create_team.html', {'players_obj': players_obj, 'keeper_form': keeper_form, 'allrounders_form': allrounders_form, 'bowlers_form': bowlers_form, 'batsmen_form': batsmen_form, 'team_created': team_created, 'user_teams_obj': user_teams_obj})

# def CreateTeamView(request, slug):'players_points': players_points,
#     print("Fiifrst Come First")
#     keeper_form = CreateTeamKeeperForm(request.POST)
#     print("after call first")
#     # team_created = False
#     # if keeper_form.is_valid():
#     #     print("form is valid")
#     #     # team_obj = IndiaWestIndiesTeam(Keeper=request.POST.get('Dinesh_Ramdin'))
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




