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
        reqs=Req_st(title=title,info=info,sender=request.user)
        reqs.save()

        return HttpResponse('ok')
    else:
        redirect('Index.html')
    return render(request,"add_re.html")



@requires_csrf_token
def view_req(request):
    waited=''
    approved=''
    # if request.user_authenticated:
    #     z=auths(request)
    #     if z==1:
    waited=Req_st.objects.filter(approved=False,sender=request.user)
    approved=Req_st.objects.filter(approved=True,sender=request.user)
        # elif z==0:
    # waited=Req_st.objects.filter(approved=False)
    # approved=Req_st.objects.filter(approved=True)
    return render(request,'view_rq.html',{'approved':approved,'waited':waited})
    # else:
    #     return redirect('login')



#
# def accept_req(request,id):
#     z=auths(request):
#     if z==0:
#         m=Req_st.objects.get(id=id)
#         for i in m:
#             i.approved=True
#         m.save()
#     return redirect('veiw_re')
#
#
# def disable_req(request,id):
#     z=auths(request):
#     if z==1:
#         a=Req_st.objects.filter(sender=request.user,id=id)
#         for i in a:
#             i.disable=True
#         a.save()
#     return redirect ('view_re')
