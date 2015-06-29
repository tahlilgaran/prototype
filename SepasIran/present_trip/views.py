from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def home_login(request):
    return render(request , 'home_login.html')

def show_one_trip(request, tour_id = '1'):
    return render(request , "one_trip.html")
# Create your views here.
