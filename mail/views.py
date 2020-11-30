from django.shortcuts import render

from .forms import *
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect


def contact_form(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # print("Valid")
            subject = f'Message Form {form.cleaned_data["name"]}'
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            # recipients =
            try:
                email = EmailMessage(
                    subject,
                    message,
                    "ramkumar.dj15@gmail.com",
                    ['ramkumarmani2000@gmail.com'],
                    reply_to=[sender]
                )
                email.send()
                print("Mail Sent")
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return HttpResponseRedirect('success/')
    context = {
        "form": form
    }
    return render(request, "contactform.html", context)


def success(request):
    return render(request, "success.html")