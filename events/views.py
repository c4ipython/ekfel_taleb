from django.shortcuts import render, redirect
from .models import Evnts
from django.http import HttpResponse
from datetime import date,timedelta
from django.views.decorators.csrf import requires_csrf_token
from accounts.views import auth


def add(request):
    if auth(request) == 1:  # admin
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
            return render(request, "add.html")
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return render(request, 'base.html')
    else:
        return render(request, 'login.html')


def viewEvents(request):
    if not auth(request) == 4:  # not a user
        yesterday = date.today() - timedelta(hours=25)
        nextyear = date.today() + timedelta(hours=7200)
        lastyear = date.today() - timedelta(hours=7200)
        lis =Evnts.objects.filter(dates__range=(date.today(),nextyear), disabled= False)
        missed = Evnts.objects.filter(dates__range=(lastyear,yesterday),disabled= False)
        return render(request, 'viewevents.html', {'list':lis, 'missed':missed})
    else:
        return render(request, 'login.html')


@requires_csrf_token
def deleted(request,id):
    if auth(request) == 1:  # admin
        if request.method == 'POST':
            idd = Evnts.objects.get(id=id)
            idd.disabled= True
            idd.save()
            return redirect("viewEvents")
        else:
            idd = Evnts.objects.get(id=id)
        return render(request, 'dltevent.html',)
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return render(request, 'base.html')
    else:
        return render(request, 'login.html')


@requires_csrf_token
def editing(request,id):
    if auth(request) == 1:  # admin
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
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return render(request, 'base.html')
    else:
        return render(request, 'login.html')
