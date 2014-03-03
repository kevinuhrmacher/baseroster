from django.shortcuts import render
from roster.models import Player, Coach, Team
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def team(request):
    team = Team.objects.all()
    return render(request, "roster/home.html", {"teams":team})

def playerList(request):
    player = Player.objects.all()
    return render(request, "roster/playerlist.html", {"players":player})
    coach = Coach.objects.all()
    return render(request, "roster/playerlist.html", {"coaches":coach})

def player(request, pk):
    player_var = Player.objects.get(id=pk)
    context ={
        "player":player_var
    }
    return render(request, "roster/player.html", context)
    

def coach(request, pk):
    coach_var = Coach.objects.get(id=pk)
    context ={
        "coach":coach_var
    }
    return render(request, "roster/coach.html", context)