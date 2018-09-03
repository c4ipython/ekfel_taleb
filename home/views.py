from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template

from home.forms import ContactForm
from django.views.decorators.csrf import requires_csrf_token


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'GET':
        form = ContactForm ()
    else:
        form = ContactForm (request.POST)
        if form.is_valid ():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail (name, message, email, ['info@example.com'])
            except BadHeaderError:
                return HttpResponse ('Invalid header found.')
            #msg = 'Success! Thank you for your message.'
            return  HttpResponse('Success! Thank you for your message.')

    return render (request, "contact.html", {'form': form })


def about(request):
    return render(request, 'about.html')
