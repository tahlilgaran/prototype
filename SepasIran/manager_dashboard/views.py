from django.shortcuts import render

# Create your views here.

def Dashboard(request):
    return render(request,"manager_dashboard.html",{"username" : "admin"})
