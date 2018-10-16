from django.shortcuts import render , redirect
from Students.models import Req_st
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from accounts.views import auth
# Create your views here.
@requires_csrf_token
def sponserRequest(request,id):
    if auth(request) == 2:  # sponsor
        if request.method == 'POST':
            a = Req_st.objects.filter(req_spon=request.user)
            aa = len(a)
            if aa < 3:
                e = Req_st.objects.get(id=id)
                e.req_spon = request.user.username
                e.save()
                return HttpResponse('donneeee')
            else:
                return HttpResponse('لا يمككن طلب اكثر من ثلاث كفالات في وقت واحد, الرجاء الانتضار لحين موافقه طلبات كفالتك')
        else:
            e = Req_st.objects.get(id=id)
        return render(request, 'req.html')
    elif auth(request) == 1 or auth(request) == 3:  # admin or student
        return redirect('home')
    else:
        return redirect('home')


@requires_csrf_token
def sponserdelete(request,id):
    if auth(request) == 2:  # sponsor
        if request.method == 'POST':
            d = Req_st.objects.get(id=id)
            d.sponser = ""
            d.save()
            return HttpResponse('donneeee')
        else:
            d = Req_st.objects.get(id=id)
        return render(request, 'del.html')
    elif auth(request) == 1 or auth(request) == 3:  # admin or student
        return redirect('home')
    else:
        return redirect('home')


@requires_csrf_token
def displayKafalat(request):
    if auth(request) == 2 or auth(request) == 1:  # sponsor or admin
        kT = Req_st.objects.filter(sponser='',req_spon='',approved = True)
        kF = Req_st.objects.filter(sponser='',req_spon='',approved = False)

        return render(request, 'kafalat.html',{'kT':kT, 'kF': kF, 'auth': auth(request)})
    else:
        return redirect('home')


@requires_csrf_token
def displayMyKafalat(request):
    if auth(request) == 2:  # sponsor
        u = request.user
        m = Req_st.objects.filter(sponser=u, approved=True,req_spon='')
        ma = Req_st.objects.filter(req_spon=u,approved=True,sponser='')
        return render(request,'myKafalat.html',{'m':m, 'ma':ma})
    elif auth(request) == 1 or auth(request) == 3:  # admin or student
        return redirect('home')
    else:
        return redirect('home')




@requires_csrf_token
def reqAdmin(request,id):
    if auth(request) == 1:  # admin
        a = Req_st.objects.get(id=id)
        if request.method == "POST":
            if 'a' in request.POST:
                    a.sponser = a.req_spon
                    a.req_spon = ""
                    a.save()
                    return HttpResponse('donneeee a')
            if 'b' in request.POST:
                    a.req_spon = ""
                    a.save()
                    return HttpResponse('donneeee b')

        return render (request, 'reqAdmin.html')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')





@requires_csrf_token
def delAdmin(request,id):
    if auth(request) == 1:  # admin
        if request.method == 'POST':
            da = Req_st.objects.get(id=id)
            da.sponser = ""
            da.save()
            return HttpResponse('donneeee da')
        return render(request, 'delAdmin.html')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')
