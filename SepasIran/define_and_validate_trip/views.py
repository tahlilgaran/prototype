from django.shortcuts import render

# Create your views here.
def tarif_kind(request,username):

    return  render(request,"tarif_kind.html",{
        'username': username,
    })