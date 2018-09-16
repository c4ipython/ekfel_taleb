from django.shortcuts import render
from Students.models import Req_st
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
@requires_csrf_token
def sponserRequest(request,id):
    if request.method == 'POST':
        e = Req_st.objects.get(id=id)
        e.req_spon = request.user.username
        e.save()
        return HttpResponse('donneeee')
    else:
        e = Req_st.objects.get(id=id)
    return render(request, 'req.html')



@requires_csrf_token
def sponserdelete(request,id):
    if request.method == 'POST':
        d = Req_st.objects.get(id=id)
        d.sponser = ""
        d.save()
        return HttpResponse('donneeee')
    else:
        d = Req_st.objects.get(id=id)
    return render(request, 'del.html')





@requires_csrf_token
def displayKafalat(request):
    k = Req_st.objects.filter(sponser='',req_spon='')
    return render(request, 'kafalat.html',{'k':k})


@requires_csrf_token
def displayMyKafalat(request):
    u = request.user
    m = Req_st.objects.filter(sponser=u)
    return render(request,'myKafalat.html',{'m':m})





@requires_csrf_token
def reqAdmin(request,id):
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




@requires_csrf_token
def delAdmin(request,id):
    if request.method == 'POST':
        da = Req_st.objects.get(id=id)
        da.sponser = ""
        da.save()
        return HttpResponse('donneeee da')
    return render(request, 'delAdmin.html')
