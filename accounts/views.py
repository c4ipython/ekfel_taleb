from django.shortcuts import render, redirect
from .models import Sponsor
from .models import Students
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.admin import User
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.


@requires_csrf_token
def signup_sponsor(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        fullName = request.POST.get("fullName")
        age = request.POST.get("age")
        birthDate = request.POST.get("birthDate")
        governorate = request.POST.get("governorate")
        job = request.POST.get("job")
        jobAddress = request.POST.get("jobAddress")
        phone = request.POST.get("phone")
        img = request.POST.get("img")
        monthlySalary = request.POST.get("monthlySalary")
        try:
            form1 = User.objects.create_user(username=username, password=password)
            form1.save()
            form2 = Sponsor(username=username, full_name=fullName, age=age, birth_date=birthDate, city=governorate, work=job, work_locations=jobAddress, number=phone, img=img, salary=monthlySalary)
            form2.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return render(request, "base.html")
        except:
            return render(request, 'signup_sponsor.html', {'msg': 'This username has already been used'})
    return render(request, 'signup_sponsor.html')


@requires_csrf_token
def logins(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'base.html', {'user': username})
        return render(request, 'login.html')


def logouts(request):
    logout(request)


@requires_csrf_token
def signup_student(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        fullName = request.POST.get("fullName")
        age = request.POST.get("age")
        birthDate = request.POST.get("birthDate")
        governorate = request.POST.get("governorate")
        stage = request.POST.get("stage")
        phone = request.POST.get("phone")
        img = request.POST.get("img")

        try:
            form1 = User.objects.create_user(username=username, password=password)
            form1.save()
            form2 = Students(username=username, full_name=fullName, age=age, birth_date=birthDate, city=governorate, stage=stage, number=phone, img=img)
            form2.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return render(request, "base.html")
        except:
            return render(request, 'signup_student.html', {'msg': 'This username has already been used'})
    return render(request, 'signup_student.html')


def auth():
    sponsor = Sponsor.objects.get(username=request.user)
    student = Students.objects.get(username=request.user)
    x = 0
    if request.user.is_authenticated and not sponsor and not student:
        x = 1  # admin
    elif request.user.is_authenticated and sponsor:
        x = 2  # sponsor
    elif request.user.is_authenticated and student:
        x = 3  # student
    else:
        x = 4  # user
    return x
