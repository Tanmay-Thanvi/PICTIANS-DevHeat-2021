from django.shortcuts import render

from workout.models import Category, Exercise, Level

def home(request):
    lvl = Level.objects.all()
    cat = Category.objects.all()
    ex = Exercise.objects.all()
    return render(request,"page2.html",{"cat":cat,"lvl":lvl,"ex":ex})

def training(request):
    return render(request,'training.html')

def schedule(request):
    day = request.GET['day']
    ex = Exercise.objects.all()
    return render(request,'schedule.html',{"day":day,"ex":ex})