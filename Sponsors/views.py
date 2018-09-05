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
    return render(request, 'req.html')
