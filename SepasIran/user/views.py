from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.


def signin(request):

    if request.POST.get("login","")!= "":
        username = request.POST.get("username")
        return HttpResponseRedirect('/userpage/'+username)
    if request.method == 'GET' :
        username = ""
    if request.POST.get("signup","") != "":
        return HttpResponseRedirect('/signup/')
    if request.POST.get("forget","") != "":
        return HttpResponseRedirect('/forgetpassword/')

    return render(request, "login.html",{
        'username':username,
    })


def forget_password(request):

    return render(request, "forget.html",{
        # 'username':username,
    })


def signup(request):

    return render(request, "signup.html",{
        # 'username':username,
    })


def tourist_signup(request,username):

    return render(request, "signup_tourist.html",{
        'username':username,
    })

def servant_signup(request,username):

    return render(request, "signup_tourBuilder.html",{
        'username':username,
    })

def edit_tourist(request,username):

    return render(request, "edit_tourist.html",{
        'username':username,
    })

def edit_tourbuilder(request,username):

    return render(request, "edit_tourbuilder.html",{
        'username':username,
    })


def tourist_profile(request,username):

    return render(request, "tourist_profile.html",{
        'username':username,
    })