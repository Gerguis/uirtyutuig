from django.conf.urls import url
from . import views

app_name = 'cricket_center'

urlpatterns = [
    url(r'^$', views.CricketCenterIndexView, name="cricket_center"),
    url(r'match/(?P<slug>[\w]+)', views.SingleMatchView, name='match')
]
