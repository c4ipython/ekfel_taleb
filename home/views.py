
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render
from home.forms import ContactForm
from django.views.decorators.csrf import requires_csrf_token
from accounts.views import auth

@requires_csrf_token
def home(request):
    return render(request, 'home.html', {'auth': auth(request)})

@requires_csrf_token
def contact(request):
    msg_er=''
    msg_ok=''
    if request.method == 'GET':
        form = ContactForm ()
    else:
        form = ContactForm (request.POST)
        if form.is_valid ():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail (name, message, email, ['info@example.com'])  #يتم وضع ايميل الخاص بالاتصال بادارة الموقع
            except BadHeaderError:
                msg_er = 'Invalid header found.'  # رسالة في حالة وجود خطأ في الايميل
                return render (request, "contact.html", {'msg_er': msg_er })
            msg_ok ='تم ارسال رسالتك بنجاح... شكرا لك'
            return  render (request,"contact.html", {'msg_ok': msg_ok })

    return render (request, "contact.html", {'form': form })

@requires_csrf_token
def about(request):
    return render(request, 'about.html')

@requires_csrf_token
def c4i(request):
    return render(request, 'c4i.html')

@requires_csrf_token
def devteam(request):
    return render(request, 'devteam.html')
