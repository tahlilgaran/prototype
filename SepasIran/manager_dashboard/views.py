from django.shortcuts import render

# Create your views here.

def Dashboard(request):
    return render(request,"manager_dashboard.html",{"username" : "admin"})


def tourLists(request):
     return render(request,"manager_tours.html",{"username" : "admin"})

def tourRating(request):
    return render(request,"manager_tours_rating.html",{"username" : "admin"})