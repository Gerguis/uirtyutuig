from django import forms


class CreateTeamKeeperForm(forms.Form):
    Dinesh_Ramdin = forms.BooleanField(required=False, initial=False)
    MS_Dhoni = forms.BooleanField(required=False, initial=False)
    Dinesh_Kartik = forms.BooleanField(required=False, initial=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        true_count = list(cleaned_data.values())
        if true_count.count(True) != 1:
            raise forms.ValidationError("Please Select only One Keeper.")


class CreateTeamBatsmenForm(forms.Form):
    Rohit_Sharma = forms.BooleanField(required=False)
    Shikhar_Dhawan = forms.BooleanField(required=False)
    Virat_Kohli = forms.BooleanField(required=False)
    Suresh_Raina = forms.BooleanField(required=False)
    Andre_Fletcher = forms.BooleanField(required=False)
    Evin_Lewis = forms.BooleanField(required=False)
    Marlon_Samuels = forms.BooleanField(required=False)
    Chadwick_Walton = forms.BooleanField(required=False)
    Shreyas_Iyer = forms.BooleanField(required=False)
    Lokesh_Rahul = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        true_count = list(cleaned_data.values())
        if true_count.count(True) > 5:
            raise forms.ValidationError("Only 5 Batsmen are Allowed")
        elif true_count.count(True) < 3:
            raise forms.ValidationError("Please, Select at Least 3 Batsmen")


class CreateTeamAllroundersForm(forms.Form):
    Hardik_Pandya = forms.BooleanField(required=False)
    Axar_Patel = forms.BooleanField(required=False)
    Andre_Russell = forms.BooleanField(required=False)
    Rovman_Powell = forms.BooleanField(required=False)
    Carlos_Brathwaite = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        true_count = list(cleaned_data.values())
        if true_count.count(True) > 3:
            raise forms.ValidationError("Only 3 Allrounder are Allowed")
        elif true_count.count(True) < 1:
            raise forms.ValidationError("Please, Select at Least 1 Allrounder")


class CreateTeamBowlersForm(forms.Form):
    Bhuvneshwar_Kumar = forms.BooleanField(required=False)
    Kuldeep_Yadav = forms.BooleanField(required=False)
    Shardul_Thakur = forms.BooleanField(required=False)
    Yuzvendra_Chahal = forms.BooleanField(required=False)
    Siddarth_Kaul = forms.BooleanField(required=False)
    Umesh_Yadav = forms.BooleanField(required=False)
    Ashley_Nurse = forms.BooleanField(required=False)
    Samuel_Badree = forms.BooleanField(required=False)
    Kesrick_Williams = forms.BooleanField(required=False)
    Keemo_Paul = forms.BooleanField(required=False)
    Sheldon_Cottrell = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        true_count = list(cleaned_data.values())
        if true_count.count(True) > 5:
            raise forms.ValidationError("Only 5 Bowlers are Allowed")
        elif true_count.count(True) < 3:
            raise forms.ValidationError("Please, Select at Least 3 Bowlers")

# class CreateCaptainViceCaptain(forms.Form):
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
