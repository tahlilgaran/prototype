from django.shortcuts import render

# Create your views here.


def userRating(request):
    return render(request, "quality_user_rating.html", {"username": "gardeshgar"})

def onlineComment(request):
    return render(request, "quality_online_comment.html", {"username": "gardeshgar"})