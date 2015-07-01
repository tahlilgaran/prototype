from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def home_login(request):
    return render(request , 'home_login.html')

def show_one_trip(request, kind = '' ,tour_id = '1'):
    if kind == 'service':
        return render(request , "one_trip.html" , {'kind':kind})
    elif kind == 'tour':
        return render(request , "one_trip.html" , {'kind':kind})
    elif kind == 'pack':
        return render(request , "one_trip.html" , {'kind':kind})

def show_one_trip_status(request , kind =''):
    return render(request , "status_trip.html")

def search(request):
    return render(request , "search_result.html")
# Create your views here.
