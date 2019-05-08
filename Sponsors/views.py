from django.shortcuts import render , redirect
from Students.models import Req_st
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from accounts.views import auth
from accounts.models import Sponsor
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.




class displayKafalatListView(LoginRequiredMixin, ListView):  #for sponser
    #context_object_name = 'kafalat'   # your own name for the list as a template variable
    template_name = 'kafalat.html'
    model = Req_st
    queryset = Req_st.objects.filter(approved = True,sponser='',req_spon='',disable = False)






class adminDisplayKafalatListView(LoginRequiredMixin, ListView):  #for admin
    template_name = 'adminKafalat.html'
    model = Req_st
    queryset = Req_st.objects.all()
    #context_object_name = 'kafalat'   # your own name for the list as a template variable
    def get_context_data(self):
        context = super(adminDisplayKafalatListView, self).get_context_data()
        context['kta'] = Req_st.objects.filter(approved = True,sponser='',req_spon='',disable = False)
        context['ktb'] = Req_st.objects.filter(approved = True,sponser='',disable = False).exclude(req_spon__exact='')
        context['ktc'] = Req_st.objects.filter(approved = True,req_spon='',disable = False).exclude(sponser__exact='')
        return context





class displayMyKafalatListView(LoginRequiredMixin, ListView):  #for sponser
    template_name = 'myKafalat.html'
    model = Req_st
    queryset = Req_st.objects.all()
    #context_object_name = 'myKafalat'   # your own name for the list as a template variable
    def get_context_data(self):
        context = super(displayMyKafalatListView, self).get_context_data()
        u = self.request.user
        context['m'] = Req_st.objects.filter(sponser=u, approved=True,req_spon='',disable = False)
        context['ma'] = Req_st.objects.filter(req_spon=u,approved=True,sponser='',disable = False)
        return context




@requires_csrf_token
def addSponserRequest(request,id):   #for sponser
    if auth(request) == 2:  # sponsor
            a = Req_st.objects.filter(req_spon=request.user,disable = False)
            aa = len(a)
            if aa < 3:
                e = Req_st.objects.get(id=id,disable = False)
                s = Sponsor.objects.get(username=request.user.username,disabled = False)
                e.req_spon = request.user.username

                e.save()
                return redirect('kafalaty')
            else:
                return HttpResponse('لا يمكن طلب اكثر من ثلاث كفالات في وقت واحد, الرجاء الانتضار لحين موافقه طلبات كفالتك')
    elif auth(request) == 1 or auth(request) == 3:  # admin or student
        return redirect('home')
    else:
        return redirect('home')





@requires_csrf_token
def sponserdelete(request,id):   #for sponser
    if auth(request) == 2:  # sponsor
            d = Req_st.objects.get(id=id,disable = False)
            d.sponser = ""
            d.req_spon = ""
            d.sNumberReq = ""
            d.sNumber = ""
            d.save()
            return redirect('kafalaty')
    elif auth(request) == 1 or auth(request) == 3:  # admin or student
        return redirect('home')
    else:
        return redirect('home')





@requires_csrf_token
def adminAncceptTheSponserRequest(request,id):   #for admin
    if auth(request) == 1:  # admin
        a = Req_st.objects.get(id=id,disable = False)
        a.sponser = a.req_spon
        a.req_spon = ""
        a.sNumber = a.sNumberReq
        a.sNumberReq = ""
        a.save()
        return redirect('kafalat')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')





@requires_csrf_token
def adminRefuseTheSponserRequest(request,id):
    if auth(request) == 1:  # admin
        a = Req_st.objects.get(id=id,disable = False)
        a.req_spon = ""
        a.sNumberReq = ""
        a.save()
        return redirect('kafalat')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')





@requires_csrf_token
def adminDeleteTheSponser(request,id):  #for admin
    if auth(request) == 1:  # admin
            da = Req_st.objects.get(id=id,disable = False)
            da.sponser = ""
            da.sNumber = ""
            da.save()
            return redirect('kafalat')
    elif auth(request) == 2 or auth(request) == 3:  # sponsor or student
        return redirect('home')
    else:
        return redirect('home')
