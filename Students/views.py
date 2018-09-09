from django.shortcuts import render
from django.http import HttpResponse
from Students.models import Req_st
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import redirect


def index(request):
    return render(request,'Index.html')



# def auths(request):
#     z=0
#     st=Student.objects.filter(username=request.user)
#     sp=Sponsor.objects.filter(username=request.user)
#     for i in st :
#         if i.types=='طالب':
#           z=1
#       else:
#           z=0
#    for i in sp:
#        if i.types=='كفيل':
#            z=2
#      else:
#          z=0
# return z
#


@requires_csrf_token
def add_req(request):
    # z=auths(request)
    # if z==1:
    #     ss=''
    if request.method=='POST':
        title=request.POST.get('title')
        info=request.POST.get('info')
        forms=Req_st(title=title,info=info,sender=request.user)
        forms.save()
        return HttpResponse('ok')
    else:
        redirect('Index.html')
    return render(request,"add_re.html")
