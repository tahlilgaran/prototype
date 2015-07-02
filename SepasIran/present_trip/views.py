from django.shortcuts import render
def home(request , username = ''):
    return render(request, 'present_trip/home.html', {'username':username})

def show_one_trip(request, kind = '' ,tour_id = '1'):
    if kind == 'service':
        return render(request , "present_trip/one_trip.html", {'kind':kind})
    elif kind == 'tour':
        return render(request , "present_trip/one_trip.html", {'kind':kind})
    elif kind == 'pack':
        return render(request , "present_trip/one_trip.html", {'kind':kind})

def show_one_trip_status(request , kind =''):
    return render(request , "present_trip/status_trip.html")

def search(request):
    return render(request , "present_trip/search_result.html")
# Create your views here.
