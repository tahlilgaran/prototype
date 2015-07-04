from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def tarif_kind(request,username =''):

    if request.POST.get("next","") != "":
        print("next")
        tour = request.POST.getlist("optradio")
        if tour:
            print("aval")
        if 1 in tour:
            print("write")
            return HttpResponseRedirect("/home/")

    return  render(request,"tarif_kind.html",{
         'username': username,
    })


def tour_define(request,username = ''):

    return render(request,"tour_define.html",{
        'username': username,
    })


def airplane_define(request,username):

    return render(request,"airplane_define.html",{
        'username': username,
    })


def train_define(request,username):

    return render(request,"train_define.html",{
        'username': username,
    })

def cancel(request,username):

    return render(request,"cancel.html",{
        'username': username,
    })