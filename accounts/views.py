from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sponsor
from .models import Students
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.admin import User
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.


def auth(request):
    sponsor = Sponsor.objects.filter(username=request.user)
    student = Students.objects.filter(username=request.user)
    print(student)
    print(sponsor)
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


@requires_csrf_token
def signup_sponsor(request):
    if auth(request) == 4:  # user
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
                try:
                    form1 = User.objects.create_user(username=username, password=password)
                    form1.save()
                except:
                       return render(request, 'signup_sponsor.html', {'msg': 'This username has already been used'})
                form2 = Sponsor(username=username, full_name=fullName, age=age, birth_date=birthDate, city=governorate, work=job, work_locations=jobAddress, number=phone, img=img, salary=monthlySalary)
                form2.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return render(request, "base.html")
            except:
                return render(request, 'signup_sponsor.html', {'msg': 'هنالك خطأ في كتابتك للمعلومات ادناه'})
        return render(request, 'signup_sponsor.html')
    else:
        return render(request, 'base.html')


@requires_csrf_token
def logins(request):
    if auth(request) == 4:  # user
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'base.html', {'user': username})
        return render(request, 'login.html')
    else:
        return render(request, 'base.html')


def logouts(request):
    if not auth(request) == 4:  # not user
        logout(request)
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')


@requires_csrf_token
def signup_student(request):
    if auth(request) == 4:  # user
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            fullName = request.POST.get("fullName")
            age = request.POST.get("age")
            birthDate = request.POST.get("birthDate")
            governorate = request.POST.get("governorate")
            stage = request.POST.get("stage")
            phone = request.POST.get("phone")
            img = request.POST.get('img')
            form1 = User.objects.create_user(username=username, password=password)
            form1.save()
            form2 = Students(username=username, full_name=fullName, age=age, birth_date=birthDate, city=governorate, stage=stage, number=phone, img=img)
            form2.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return render(request, "base.html",{'msg':'registered'})
        return render(request, 'signup_student.html')

    else:
        return render(request, 'base.html')
