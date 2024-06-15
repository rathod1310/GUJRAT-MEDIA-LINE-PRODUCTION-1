from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index(request): 
	return render(request, 'index.html')

def about(request): 
	return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        Contact_Us.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        # Send email with the submitted details
        send_mail(
            'New Contact Form Submission',
            f'Name: {request.POST["name"]}\nEmail: {request.POST["email"]}\nSubject: {request.POST["subject"]}\nMessage: {request.POST["message"]}',
            'kanudorathod999@gmail.com',  # Sender's email address
            ['gujratlineproduction@gmail.com'],  # Recipient's email address
            fail_silently=False,
        )
        messages.success(request, 'Your message has been submitted successfully. We will get back to you soon.')
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')

def service(request): 
	return render(request, 'service.html')

def movies(request):
	movie = Movie.objects.all()
	return render(request, 'movies.html',{'movie':movie})

def serials(request): 
	serial = Serial.objects.all()
	return render(request, 'serials.html',{'serial':serial})

def advertisements(request): 
	advertisement = Advertisement.objects.all()
	return render(request, 'advertisements.html',{'advertisement':advertisement})

def web_series(request): 
	web_serie = Web_series.objects.all()
	return render(request, 'web_series.html',{'web_serie':web_serie})