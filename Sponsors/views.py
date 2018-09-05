from django.shortcuts import render
from Students.models import Req_st
from django.http import HttpResponse
# Create your views here.

def sponserRequest(request,id):
    if request.method == 'POST':
        e = Req_st.objects.get(id=id)
        e.req_spon = request.user.username
        e.save()
        return HttpResponse('donneeee')
    else:
        e = Req_st.objects.get(id=id)
    return render(request, 'req.html')
