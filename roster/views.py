from django.shortcuts import render
from roster.models import Player, Coach
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    context = {
        'player_count': Player.objects.count(),
        'coach_count': Coach.objects.count(),  
    }
    return render(request, "roster/home.html", context)

def player(request, pk):
    return render(request, "roster/player.html")

def playerList(request, pk):
    player = get_object_or_404(Player, id=pk)
    return render(request, "roster/playerlist.html")

def coach(request, pk):
    coach = get_object_or_404(Coach, id=pk)
    return render(request, "roster/coach.html", {'coach':coach})