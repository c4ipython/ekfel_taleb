from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from Students.models import Req_st
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import redirect
from accounts.views import auth







@requires_csrf_token
def add_req(request):
    if auth(request) == 3:  # student
        if request.method=='POST':
              y=Req_st.objects.filter(approved=False,disable=False)
              if len(y) < 3:
                  title=request.POST.get('title')
                  info=request.POST.get('info')
                  reqs=Req_st(title=title,info=info,sender=request.user)
                  reqs.save()
                  return redirect('view_rq')
              else:
                 return redirect('home')

        else:
            redirect('home')
        return render(request,"add_re.html")
    else:
        return redirect('home')







@requires_csrf_token
def view_req(request):
    if auth(request) == 3:  # student
        waited=''
        approved=''
        sponsed=''
        waited=Req_st.objects.filter(approved=False,sender=request.user,disable=False)
        approved=Req_st.objects.filter(approved=True,sender=request.user,sponser='',disable=False)
        sponsed=Req_st.objects.filter(approved=True,sender=request.user,disable=False)
        return render(request,'view_rq.html',{'approved':approved,'waited':waited , 'auth':auth(request)})
    elif auth(request) == 1:  # admin
        waited=Req_st.objects.filter(approved=False,disable=False)
        approved=Req_st.objects.filter(approved=True, sponser='',disable=False)
        sponsed=Req_st.objects.filter(approved=True,disable=False).exclude(sponser__exact='')
        return render(request,'view_rq.html',{'sponsed':sponsed,'approved':approved,'waited':waited ,'auth':auth(request)})

    # elif auth(request) == 2:  # sponsor
    #     return redirect('home')
    else:
        return redirect('home')






@requires_csrf_token
def accept_req(request,id):
    if auth(request) == 1:  # admin
        # z=auths(request):
        # if z==0:
        d=Req_st.objects.get(id=id)
        d.approved=True
        d.save()
        return redirect('view_rq')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')

@requires_csrf_token
def disable_req(request,id):
    if auth(request) == 3 :  # student
         a=Req_st.objects.get(sender=request.user,id=id)

         a.disable=True
         a.save()

         return  redirect('view_rq')
    elif auth(request) == 1 :  #admin
         a=Req_st.objects.get(id=id)

         a.disable=True
         a.save()

         return  redirect('view_rq')

    else:
        return redirect('home')




@requires_csrf_token
def edit_req(request,id):
    if auth(request) == 3:  # student
        m=Req_st.objects.get(sender=request.user ,id=id)

        if request.method=='POST':
            m.title=request.POST.get('title')
            m.info=request.POST.get('info')
            m.save()
            return redirect('view_rq')
            print(m)
        return render(request,'edit_re.html',{'m':m})
    elif auth(request) == 2 or auth(request) == 1:  # sponsor or admin
        return redirect('home')
    else:
        return redirect('home')
