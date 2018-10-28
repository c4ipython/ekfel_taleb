from django.shortcuts import render, redirect
from .models import Sponsor
from .models import Students
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.admin import User
from django.views.decorators.csrf import requires_csrf_token
from accounts.forms import StudentForm
from accounts.forms import SponsorForm
from Students.models import Req_st
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
                    return render(request, 'signup_sponsor.html', {'form': form2, 'msg': 'هنالك خطأ في كتابتك للمعلومات ادناه'})

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
        student = Students.objects.filter(username=request.user)
        return render(request, 'profile.html', {'student': student})
    elif auth(request) == 2 or auth(request) == 5:  # sponsor
        sponsor = Sponsor.objects.filter(username=request.user)
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


# نظام اداره الطلبه يعرضهم بشكل جداول 
# ويمكن الموافقه وحذف الحسابات من خلاله


def students(request):
    if auth(request) == 1: # admin
        student_app = Students.objects.filter(approved=True)[::-1]
        student_not_app = Students.objects.filter(approved=False)[::-1]
        if request.method == 'POST' and request.POST['search']:
            student_app = student_app.filter(username__icontains=request.POST['search'])
            student_not_app = student_not_app.filter(username__icontains=request.POST['search'])
        return render(request, 'students.html', {'formStudentA': student_app, 'formStudentN': student_not_app})
    else:
        return redirect('home')



#  عمليه حذف الحساب الطالب 

def delAppStudent(request, idd):
    if auth(request) == 1: # admin
        student = Students.objects.get(id=idd, approved=True)
        print(student)
        student.approved = False
        student.save()
        return redirect('students')
    else:
        return redirect('home')


# عمليه حذف حساب الكفيل
def delAppSponsor(request, idd):
    if auth(request) == 1: # admin
        sponsor = Sponsor.objects.get(id=idd, approved=True)
        sponsor.approved = False
        sponsor.save()
        return redirect('sponsors')
    else:
        return redirect('home')


# عرض جميع طلبات طالب معين 
# وعرضهم بشكل مفصل من طلبات مقبوله وطلبات مكفوله وطلبات غير مكفوله 
def stuReq(request, usernames):
    if auth(request) == 1: # admin
        not_sponsor = Req_st.objects.filter(sender=usernames, sponser='',disable=False).exclude(approved=False)[::-1]
        sponsor = Req_st.objects.filter(sender=usernames, disable=False).exclude(sponser='')[::-1]
        not_app = Req_st.objects.filter(sender=usernames, approved=False, disable=False)[::-1]
        is_app = Req_st.objects.filter(sender=usernames, approved=True, disable=False)[::-1]
        return render(request, 'view_re.html', {'not_sponsor': not_sponsor, 'sponsor': sponsor, 'not_app': not_app, 'is_app': is_app})
    else:
        return redirect('home')


# عرض جميع كفالات كفيل معين 
# وعرضهم بشكل مفصل من كفالات بانتظار الموافقه وكفالاته التي تمت الموافقه عليها سابقا 
def sponsor_stuReq(request, usernames):
    if auth(request) == 1: # admin
        is_sponsor = Req_st.objects.filter(sponser=usernames, approved=True).exclude(disable=True)[::-1]
        is_req = Req_st.objects.filter(req_spon=usernames, approved=True, sponser='').exclude(disable=True)[::-1]
        return render(request, 'view_sponsor.html', {'is_sponsor': is_sponsor, 'is_req': is_req})
    else:
        return redirect('home')


# اظهار معلومات طالب معين
# مع خاصيه تفعيل او الغاء تفعيل واوبشن لعرض طلباته  
def info(request, id):
    if auth(request) == 1: # admin
        student = Students.objects.filter(id=id)
        return render(request, 'profile.html', {'student': student, 'ise': True})
    else:
        return redirect('home')


# اظهار معلومات كفيل معين 
# مع خاصيه تفعيل او الغاء التفعيل واوبشن لعرض كفالاته
def sponsor_info(request, id):
    if auth(request) == 1: # admin
        sponsor = Sponsor.objects.filter(id=id)
        return render(request, 'profile.html', {'sponsor': sponsor, 'ise': True})
    else:
        return redirect('home')


# عمليه تفعيل حساب طالب معين
def add_app(request, usernamee):
    if auth(request) == 1: # admin
        student = Students.objects.get(username=usernamee, approved=False)
        student.approved = True
        student.save()
        return redirect('students')
    else:
        return redirect('home')

# عمليه تفعيل حساب كفيل معين 
def add_appSponsor(request, usernamee):
    if auth(request) == 1: # admin
        sponsor = Sponsor.objects.get(username=usernamee, approved=False)
        sponsor.approved = True
        sponsor.save()
        return redirect('sponsors')
    else:
        return redirect('home')


#  نظام عرض جميع الكفلاء بصوره جداول 
# والتي من خلاله يمكننا تفعيل حسابات والغاء حسابات ومتابعة الحسابات 
def sponsors(request):
    if auth(request) == 1: # admin
        sponsor_app = Sponsor.objects.filter(approved=True)[::-1]
        sponsor_not_app = Sponsor.objects.filter(approved=False)[::-1]
        if request.method == 'POST' and request.POST['search']:
            sponsor_app = sponsor_app.filter(username__icontains=request.POST['search'])
            sponsor_not_app = sponsor_not_app.filter(username__icontains=request.POST['search'])
        return render(request, 'sponsors.html', {'formsponsorA': sponsor_app, 'formsponsorN': sponsor_not_app})
    else:
        return redirect('home')


# قبول طلب طالب معين
def ac_req(request, id):
    if auth(request) == 1: # admin
        req = Req_st.objects.get(id=id)
        req.approved = True
        req.save()
        return redirect('students')
    else:
        return redirect('home')


# حذف طلب طالب معين 
def del_req(request, id):
    if auth(request) == 1: # admin
        req = Req_st.objects.get(id=id)
        req.disable = True
        req.save()
        return redirect('students')
    else:
        return redirect('home')



# حذف كفاله كفيل معين
def del_sponsor(request, id):
    if auth(request) == 1: # admin
        req = Req_st.objects.get(id=id)
        req.sponser = ''
        req.req_spon = ''
        req.save()
        return redirect('students')
    else:
        return redirect('home')



# قبول طلب كفل كفيل معين 
def ac_sponsor(request, id):
    if auth(request) == 1: # admin
        req = Req_st.objects.get(id=id)
        req.sponser = req.req_spon
        req.req_spon = ''
        req.save()
        return redirect('sponsors')
    else:
        return redirect('home')



# حذف طلب من صفحه الكفيل وارجاعه الصفحه الكفلاء 
def del_req_spon(request, id):
    if auth(request) == 1: # admin
        req = Req_st.objects.get(id=id)
        req.disable = True
        req.save()
        return redirect('sponsors')
    else:
        return redirect('home')



# حذف كفاله كفيل معين
def del_sponsor_req(request, id):
    if auth(request) == 1: # admin
        req = Req_st.objects.get(id=id)
        req.sponser = ''
        req.req_spon = ''
        req.save()
        return redirect('sponsors')
    else:
        return redirect('home')

