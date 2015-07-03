from django.shortcuts import render

# Create your views here.

def Dashboard(request):
    return render(request, "manager_dashboard.html", {"username": "admin"})


def tourLists(request):
    return render(request, "manager_tours.html", {"username": "admin"})


def tourRating(request):
    return render(request, "manager_tours_rating.html", {"username": "admin"})


def onlineComments(request):
    return render(request, "online_comments.html", {"username": "admin"})


def userLists(request):
    return render(request, "manager_gardeshgar_info.html", {"username": "admin"})



def paymentLists(request):
    return render(request, "manager_paymentList.html", {"username": "admin"})

def contractPercent(request):
    return render(request, "contract_percent.html", {"username": "admin"})