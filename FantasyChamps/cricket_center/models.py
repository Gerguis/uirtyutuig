from django.db import models
from .generators import MatchSlugGenerator, ContestSlugGenerator
import ast


class MatchDetail(models.Model):
    match_name = models.CharField(max_length=100)
    tournament_name = models.CharField(max_length=25)
    match_date = models.DateTimeField()
    match_tick = models.IntegerField(blank=True)
    match_slug = models.CharField(max_length=25, unique=True, default="Test")
    team_one = models.CharField(max_length=25)
    team_two = models.CharField(max_length=25)
    team_one_image = models.CharField(max_length=25)
    team_two_image = models.CharField(max_length=25)

    def save(self, *args, **kwargs):
        print(self.match_date)
        print(self.match_date.timestamp())
        self.match_tick = self.match_date.timestamp()
        if self.match_slug == "Test":
            self.match_slug = MatchSlugGenerator(self.match_name, self.team_one, self.team_two, self.match_date)
        super(MatchDetail, self).save(*args, **kwargs)

    def __str__(self):
        return self.match_name


class PlayerDetail(models.Model):
    player_name = models.CharField(max_length=255, default="")
    player_current_team = models.CharField(max_length=25, default="")
    player_type = models.CharField(max_length=25, default="Keeper/Batsman/Allrounder/Bowler")
    current_points = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    player_credit_points = models.DecimalField(max_digits=3, decimal_places=1, default=7.5)

    def __str__(self):
        return self.player_name


class ContestDetail(models.Model):
    contest_of_match = models.ForeignKey(MatchDetail)
    contest_name = models.CharField(max_length=100)
    contest_slug = models.CharField(max_length=512, unique=True, default="Test")
    contest_price = models.IntegerField()
    contest_fee = models.IntegerField()
    contest_size = models.IntegerField()
    total_player_joined = models.IntegerField()
    joined_percentage = models.IntegerField(default=0)
    contest_category = models.CharField(max_length=100)
    filled_status = models.BooleanField(default=False)
    bonus_contest = models.BooleanField(default=False)
    free_contest = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        joined = JoiningDetail.objects.filter(joined_contest_slug__exact=self.contest_slug)
        self.total_player_joined = joined.count()
        self.joined_percentage = (self.total_player_joined * 100) / self.contest_size
        if self.contest_slug == "Test":
            self.contest_slug = ContestSlugGenerator(self.contest_name, self.contest_category, self.contest_price, self.contest_fee)
        super(ContestDetail, self).save(*args, **kwargs)


    def __str__(self):
        return self.contest_slug


class JoiningDetail(models.Model):
    joined_user = models.CharField(max_length=255)
    joined_contest_slug = models.CharField(max_length=255)
    joined_user_team = models.CharField(max_length=255)
    match_slug = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.joined_contest_slug + self.joined_user_team



class IndiaWestIndiesTeam(models.Model):
    team_no = models.IntegerField(default=1)
    username_of_player = models.CharField(max_length=64)
    match_slug = models.CharField(max_length=100)
    Captain = models.CharField(max_length=255, default=" ")
    Vice_Captain = models.CharField(max_length=255, default=" ")
    Keeper = models.CharField(max_length=255, default="")
    Player2 = models.CharField(max_length=255, default="")
    Player3 = models.CharField(max_length=255, default="")
    Player4 = models.CharField(max_length=255, default="")
    Player5 = models.CharField(max_length=255, default="")
    Player6 = models.CharField(max_length=255, default="")
    Player7 = models.CharField(max_length=255, default="")
    Player8 = models.CharField(max_length=255, default="")
    Player9 = models.CharField(max_length=255, default="")
    Player10 = models.CharField(max_length=255, default="")
    Player11 = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def __unicode__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"


class IrelandAfganistan(models.Model):
    team_no = models.IntegerField(default=1)
    username_of_player = models.CharField(max_length=64)
    match_slug = models.CharField(max_length=100)
    Captain = models.CharField(max_length=255, default=" ")
    Vice_Captain = models.CharField(max_length=255, default=" ")
    Keeper = models.CharField(max_length=255, default="")
    Player2 = models.CharField(max_length=255, default="")
    Player3 = models.CharField(max_length=255, default="")
    Player4 = models.CharField(max_length=255, default="")
    Player5 = models.CharField(max_length=255, default="")
    Player6 = models.CharField(max_length=255, default="")
    Player7 = models.CharField(max_length=255, default="")
    Player8 = models.CharField(max_length=255, default="")
    Player9 = models.CharField(max_length=255, default="")
    Player10 = models.CharField(max_length=255, default="")
    Player11 = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    def __unicode__(self):
        return self.username_of_player + "[" + str(self.team_no) + "]"

    # Rohit_Sharma = models.CharField(max_length=255, default="{'Picked':False, Player_Id':1, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")  # on/off,
    # Shikhar_Dhawan = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':2, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Virat_Kohli = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':3, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Dinesh_Karthik = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':4, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Suresh_Raina = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':5, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Hardik_Pandya = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':7, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Bhuvneshwar_Kumar = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':8, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Kuldeep_Yadav = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':9, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Shardul_Thakur = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':10, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Yuzvendra_Chahal = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':11, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Shreyas_Iyer = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':12, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Axar_Patel = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':13, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Siddarth_Kaul = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':14, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Lokesh_Rahul = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':15, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Umesh_Yadav = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':16, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Andre_Fletcher = models.CharField(max_length=255, default="{'Picked':False, Player_Id':1, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")  # on/off,
    # Evin_Lewis = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':2, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Andre_Russell = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':3, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Marlon_Samuels = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':4, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Rovman_Powell = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':5, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    #Denesh_Ramdin = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':6, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Carlos_Brathwaite = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':7, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Ashley_Nurse = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':8, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Samuel_Badree = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':9, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Keemo_Paul = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':10, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Kesrick_Williams = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':11, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Chadwick_Walton = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':12, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
    # Sheldon_Cottrell = models.CharField(max_length=255, default="{'Picked':False, 'Player_Id':13, 'Team':'India', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")

# Keeper_Dict = list(keeper_form.cleaned_data.keys())[list(keeper_form.cleaned_data.values()).index(True)]
#  Selected_Keeper = {'Player': Selected_Keeper, 'Team': '', 'Captain': False, 'Vice_Captain': False, 'Current_Points': 0, 'Total_Points': 0}
#             Selected_Batsmen = [k for k, v in batsmen_form.cleaned_data.items() if v is True]
#             Selected_Allrounders = [k for k, v in allrounders_form.cleaned_data.items() if v is True]
#             Selected_Bowlers = [k for k, v in bowlers_form.cleaned_data.items() if v is True]
#             list_of_players = [str(Selected_Keeper)] + []
#             for Batsman in Selected_Batsmen:
#                 scalton_dict = {'Player': Batsman, 'Team': '', 'Captain': False, 'Vice_Captain': False, 'Current_Points': 0, 'Total_Points': 0}
#                 list_of_players = list_of_players.append(str(scalton_dict))

#             for Allrounders in Selected_Allrounders:
#                 scalton_dict = {'Player': Allrounders, 'Team': '', 'Captain': False, 'Vice_Captain': False, 'Current_Points': 0, 'Total_Points': 0}
#                 list_of_players = list_of_players.append(str(scalton_dict))
            
#             for Bowler in Selected_Bowlers:
#                 scalton_dict = {'Player': Bowler, 'Team': '', 'Captain': False, 'Vice_Captain': False, 'Current_Points': 0, 'Total_Points': 0}
#                 list_of_players = list_of_players.append(str(scalton_dict))
#             team_obj = IndiaPakistanTeam(
#                                             team_no=new_team_no,
#                                             username_of_player=request.user.username,
#                                             match_slug=slug,
#                                             Keeper = models.CharField(max_length=255, default="")
#     Player2 = models.CharField(max_length=255, default="{'Player':'Anon', 'Team':'', 'Captain':False, 'Vice_Captain':False, 'Current_Points':0, 'Total_Points':0}")
#     Player3 = models.CharField(max_length=255, default="")
#     Player4 = models.CharField(max_length=255, default="")
#     Player5 = models.CharField(max_length=255, default="")
#     Player6 = models.CharField(max_length=255, default="")
#     Player7 = models.CharField(max_length=255, default="")
#     Player8 = models.CharField(max_length=255, default="")
#     Player9 = models.CharField(max_length=255, default="")
#     Player10 = models.CharField(max_length=255, default="")
#     Player11
