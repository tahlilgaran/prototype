from django.shortcuts import render

# Create your views here.
def payment(request):

    return render(request, "payment_bank.html")

def confirm(request):

    return render(request, "transaction-status.html")

def cancel(request ,kind=''):

    if kind == 'service':
        return render(request , "canceling.html", {'kind':kind})
    elif kind == 'tour':
        return render(request, "canceling.html" , {'kind':kind})
    elif kind == 'confirm':
        return render(request, "canceling.html" , {'kind':kind})

