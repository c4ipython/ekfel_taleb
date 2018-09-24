from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sponsor
from .models import Students
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.admin import User
from django.views.decorators.csrf import requires_csrf_token
from accounts.forms import StudentForm
from accounts.forms import SponsorForm
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
        form2 = SponsorForm()
        if request.method == 'POST':
            form1 = User.objects.filter(username=request.POST['username'])
            if not form1:
                form1 = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                form1.save()
                form2 = SponsorForm(request.POST, request.FILES)
                if form2.is_valid():
                    form2.save()
                    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                    login(request, user)
                else:
                    form1 = User.objects.filter(username=request.POST['username'])
                    logout(request)
                    form1.delete()
                    return render(request, 'signup_sponsor.html', {'msg': 'هنالك خطأ في كتابتك للمعلومات ادناه'})

                return render(request, "base.html", {'msg': 'registered'})
            else:
                return render(request, 'signup_sponsor.html', {'form': form2, 'msg': 'This username has already been used'})

        return render(request, 'signup_sponsor.html', {'form': form2})

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
        form2 = StudentForm()
        if request.method == 'POST':
            form1 = User.objects.filter(username=request.POST['username'])
            if not form1:
                form1 = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                form1.save()
                form2 = StudentForm(request.POST, request.FILES)
                if form2.is_valid():
                    form2.save()
                    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                    login(request, user)
                else:
                    form1 = User.objects.filter(username=request.POST['username'])
                    logout(request)
                    form1.delete()
                    return render(request, 'signup_student.html', {'msg': 'هنالك خطأ في كتابتك للمعلومات ادناه'})

                return render(request, "base.html", {'msg': 'registered'})
            else:
                return render(request, 'signup_student.html', {'form': form2, 'msg': 'This username has already been used'})

        return render(request, 'signup_student.html', {'form': form2})

    else:
        return render(request, 'base.html')


def profile(request):
    if auth(request) == 3:  # student
        student = Students.objects.get(username=request.user)
        return render(request, 'profile.html', {'student': student})
    elif auth(request) == 2:  # sponsor
        sponsor = Sponsor.objects.get(username=request.user)
        return render(request, 'profile.html', {'sponsor': sponsor})
    elif auth(request) == 1:  # admin
        return render(request, 'base.html')
    else:
        return render(request, 'login.html')


