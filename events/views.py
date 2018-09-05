from django.shortcuts import render
from . import models
from django.http import HttpResponse


def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        details = request.POST.get("details")
        address=request.POST.get("address")
        source=request.POST.get("source")
        dates=request.POST.get("dates")
        user = request.user
        form = models.Evnts(title=title, details= details, address=address, source=source, dates= dates, username= user)
        form.save()
        return HttpResponse("good")
    else:
        return render(request,"add.html")
