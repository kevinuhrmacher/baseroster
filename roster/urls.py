from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='roster_home'),
    
    url(r'^player/$', views.player, name='roster_player'),
   
    url(r'^player/(?P<pk>\d+)$', views.player, name='roster_player'),
    url(r'^coach/(?P<pk>\d+)$', views.coach, name='roster_coach'),
    )