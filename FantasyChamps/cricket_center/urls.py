from django.conf.urls import url
from . import views

app_name = 'cricket_center'

urlpatterns = [
    url(r'^$', views.CricketCenterIndexView, name="cricket_center"),
    url(r'match/(?P<slug>[\w]+)', views.SingleMatchView, name='match'),
    url(r'create_team/(?P<slug>[\w]+)', views.CreateTeamView, name='create_team'),
    url(r'(?P<match_slug>[\w]+)/(?P<contest_slug>[\w]+)/join_now_contest', views.ContestJoinNow, name='join_now_contest'),
    url(r'^pay_and_join/', views.PayAndJoin, name='pay_and_join'),
    url(r'^proceed_to_pay/', views.ProceedToPay, name='proceed_to_pay'),
]
