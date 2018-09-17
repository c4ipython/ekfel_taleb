from django.shortcuts import render, redirect
from .models import Evnts
from django.http import HttpResponse
from datetime import date,timedelta
from django.views.decorators.csrf import requires_csrf_token


def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        details = request.POST.get("details")
        address=request.POST.get("address")
        source=request.POST.get("source")
        dates=request.POST.get("dates")
        user = request.user
        form = Evnts(title=title, details= details, address=address, source=source, dates= dates, username= user)
        form.save()
        return HttpResponse("good")
    else:
        return render(request,"add.html")


def viewEvents(request):
    yesterday = date.today() - timedelta(hours=25)
    nextyear = date.today() + timedelta(hours=7200)
    lastyear = date.today() - timedelta(hours=7200)
    lis =Evnts.objects.filter(dates__range=(date.today(),nextyear), disabled= False)
    missed = Evnts.objects.filter(dates__range=(lastyear,yesterday),disabled= False)
    return render(request, 'viewevents.html',{'list':lis, 'missed':missed})


@requires_csrf_token
def deleted(request,id):
    if request.method == 'POST':
        idd = Evnts.objects.get(id=id)
        idd.disabled= True
        idd.save()
        return redirect("viewEvents")
    else:
        idd = Evnts.objects.get(id=id)
    return render(request, 'dltevent.html',)



@requires_csrf_token
def editing(request,id):
    idd = Evnts.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get("title")
        details = request.POST.get("details")
        address=request.POST.get("address")
        source=request.POST.get("source")
        dates=request.POST.get("dates")
        idd.title = title
        idd.details = details
        idd.address = address
        idd.source = source
        idd.dates = dates
        idd.save()
        return redirect("viewEvents")
    else:
        idd = Evnts.objects.get(id=id)
    return render(request, 'editEvents.html',{'form': idd})
