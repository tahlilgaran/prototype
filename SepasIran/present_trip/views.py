from django.shortcuts import render
def home(request , username = ''):
    return render(request, 'present_trip/home.html', {'username':username})

def show_one_trip(request, kind = '' ,username = ''):
    if kind == 'service':
        return render(request , "present_trip/one_trip.html", {'kind':kind , 'username':username})
    elif kind == 'tour':
        return render(request , "present_trip/one_trip.html", {'kind':kind , 'username':username})
    elif kind == 'pack':
        return render(request , "present_trip/one_trip.html", {'kind':kind , 'username':username})

def show_one_trip_status(request , kind = '' , username = ''):
    return render(request , "present_trip/status_trip.html" , {'username':username , 'kind':kind})

def search(request , username = '' , ispack = ''):

    return render(request , "present_trip/search_result.html" , {'username':username , 'ispack':ispack})

def start_search(request , username =''):
    return render(request,"present_trip/search.html" , {'username':username})
# Create your views here.
