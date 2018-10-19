from django.shortcuts import render, redirect
from .models import Sponsor
from .models import Students
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.admin import User
from django.views.decorators.csrf import requires_csrf_token
from accounts.forms import StudentForm
from accounts.forms import SponsorForm
# Create your views here.

# اعطاء صلاحيه لكل مستخدم حسب موقعه وحمايه الموقع من التلاعب 

def auth(request):
    sponsor_approved = Sponsor.objects.filter(username=request.user)
    student_approved = Students.objects.filter(username=request.user)
    x = 0
    if request.user.is_authenticated and not sponsor_approved and not student_approved:
        x = 1  # admin
    elif request.user.is_authenticated and sponsor_approved:
        sponsor_approved = sponsor_approved.filter(approved=True)
        if sponsor_approved:
            sponsor_approved = sponsor_approved.filter(disabled=True)
            if sponsor_approved:
                x = 0  # disabled account
            else:
                x = 2  # sponsor
        else:
            x = 5  # sponsor don't have approved
    elif request.user.is_authenticated and student_approved:
        student_approved = student_approved.filter(approved=True)
        if student_approved:
            student_approved = student_approved.filter(disabled=True)
            if student_approved:
                x = 0  # disabled account
            else:
                x = 3  # student
        else:
            x = 6  # student don't have approved
    else:
        x = 4  # user
    return x

# تسجيل دخول الخاص بحسابات الكفلاء وارسالهم الى الصفحه الرئيسيه
#  بعد اتمام عمليه التسجيل للانتظار
# لحين التأكد من المعلومات الخاصه بهم وموافقه على حسابات
@requires_csrf_token
def signup_sponsor(request):
    if auth(request) == 4:  # user
        form2 = SponsorForm()
        if request.method == 'POST':
            # التاكد من ان اليوزر غير موجود في قاعدة البيانات لمنع وجود الاخطاء او التكرار
            form1 = User.objects.filter(username=request.POST['username'])
            if not form1:
                form1 = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                form1.save()
                form2 = SponsorForm(request.POST, request.FILES)
                if form2.is_valid():
                    form2.save()
                    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                    login(request, user)
                    return redirect('home')
                else:
                    form1 = User.objects.filter(username=request.POST['username'])
                    logout(request)
                    form1.delete()
                    return render(request, 'signup_sponsor.html', {'msg': 'هنالك خطأ في كتابتك للمعلومات ادناه'})

            else:
                return render(request, 'signup_sponsor.html', {'form': form2, 'msg': 'This username has already been used'})

        return render(request, 'signup_sponsor.html', {'form': form2})

    else:
        return redirect('home')

# تسجيل دخول الى الحسابات باستخدام اليوزر والباسورد
@requires_csrf_token
def logins(request):
    if auth(request) == 4:  # user
        student = ''
        sponsors = ''
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            # للتأكد ان هذا الحساب موجود بلفعل في قاعده البيانات
            if user is not None:

                login(request, user)
                student = Students.objects.filter(username=request.user, disabled=True)
                sponsors = Sponsor.objects.filter(username=request.user, disabled=True)
                # للتأكد ان هذا الحساب غير متوقف 
                if not student and not sponsors: 
                    return redirect('home')
                else:
                    logout(request)
                    return render(request, 'login.html', {'msg': 'هذا الحساب متوقف عن العمل لا يمكن تسجيل دخول اليه'})
            else:
                return render(request, 'login.html', {'msg': 'لديك خطأ في كلمه السر او اسم المستخدم يرجى التأكد'})

        return render(request, 'login.html')
    else:
        return redirect('home')

# عمليه تسجيل الخروج مع صلاحيه والتي تعمل مع الاشخاص المسجلين داخل الموقع 
def logouts(request):
    if not auth(request) == 4:  # not user
        logout(request)
        return redirect('home')
    else:
        return redirect('home')

# تسجيل ك طالب من خلال اليوزر والباسورد ومعلومات اخرى خاصه 
# ويتم نقله الى الصفحه الرئيسيه للانتظار 
#لحين التأكد من معلوماته ويتم الموافقه على حسابه 
@requires_csrf_token
def signup_student(request):
    if auth(request) == 4:  # user
        form2 = StudentForm()
        if request.method == 'POST':
            form1 = User.objects.filter(username=request.POST['username'])
            # للتاكد من عدم وجود مثل هذا الحساب في قاعدة البيانات 
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

                return redirect('home')
            else:
                return render(request, 'signup_student.html', {'form': form2, 'msg': 'This username has already been used'})

        return render(request, 'signup_student.html', {'form': form2})

    else:
        return redirect('home')

# اظهار المعلومات الشخصيه للمستخدمين مع صلاحيه لمنع التلاعب 
def profile(request):
    if auth(request) == 3 or auth(request) == 6:  # student
        student = Students.objects.get(username=request.user)
        return render(request, 'profile.html', {'student': student})
    elif auth(request) == 2 or auth(request) == 5:  # sponsor
        sponsor = Sponsor.objects.get(username=request.user)
        return render(request, 'profile.html', {'sponsor': sponsor})
    else:
        return redirect('home')

# حذف الحسابات وهو بلاصل ليس الحذف وانما تعطيله ليتم الاستفاده من اسباب الحذف 
# ويتم الحذف حسب صلاحيه المستخدم 
def delete_account(request):
    if auth(request) == 3 or auth(request) == 6:  # student
        student = Students.objects.get(username=request.user)
        student.disabled = True
        student.save()
        logout(request)
        return redirect('home')
        
    elif auth(request) == 2 or auth(request) == 1:  # sponsor
        sponsor = Sponsor.objects.get(username=request.user)
        sponsor.disabled = True
        sponsor.save()
        logout(request)
        return redirect('home')
    else:
        return redirect('home')

