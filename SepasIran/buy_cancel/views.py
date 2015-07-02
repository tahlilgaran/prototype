from django.shortcuts import render

# Create your views here.
def purchase(request ,kind=''):

    if kind == 'service':
        return render(request , "information_of_buyer_service.html")
    elif kind == 'tour':
        return render(request, "information_of_buyer_tour.html" )




def reserve(request ,kind=''):

    if kind == 'service':
        return render(request , "information_of_reserver_service.html")
    elif kind=='confirm':
         return render(request, "reservation-status.html")
    elif kind== 'tour':
        return render(request, "information_of_reserver_tour.html" )

#def confirmreserve(request):

   #  c.update(csrf(request))

   # return render_to_response("reservation-status.html", c)
