from django.shortcuts import render
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
    else:
        return HttpResponse('لا يمكنك الدخول الى هنا')


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
    else:
        return HttpResponse('لا يمكنك الدخول الى هنا')


@requires_csrf_token
def displayKafalat(request):
    if auth(request) == 2:  # sponsor
        k = Req_st.objects.filter(sponser='',req_spon='')
        return render(request, 'kafalat.html',{'k':k})
    else:
        return HttpResponse('لا يمكنك الدخول الى هنا')


@requires_csrf_token
def displayMyKafalat(request):
    if auth(request) == 2:  # sponsor
        u = request.user
        m = Req_st.objects.filter(sponser=u)
        return render(request,'myKafalat.html',{'m':m})
    else:
        return HttpResponse('لا يمكنك الدخول الى هنا')




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
    else:
        return HttpResponse('لا يمكنك الدخول الى هنا')





@requires_csrf_token
def delAdmin(request,id):
    if auth(request) == 1:  # admin
        if request.method == 'POST':
            da = Req_st.objects.get(id=id)
            da.sponser = ""
            da.save()
            return HttpResponse('donneeee da')
        return render(request, 'delAdmin.html')
    else:
        return HttpResponse('لا يمكنك الدخول الى هنا')
