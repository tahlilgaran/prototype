from django.shortcuts import render

# Create your views here.
def payment(request):

    return render(request, "payment_bank.html")

def confirm(request):

    return render(request, "transaction-status.html")