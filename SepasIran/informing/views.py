from django.shortcuts import render
def account(requst, username = ''):
    return render(requst , 'informing/account.html' , {'username':username})

