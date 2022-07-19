from django.shortcuts import render
import datetime
from django.http import HttpResponse

def index(request):
    a = datetime.datetime.now()
    return render (request, "newyearapp/new.html", {
        "newyear" : a.day == 1 and a.month == 1
    })

    

# Create your views here.
