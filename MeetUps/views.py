from django.shortcuts import render
from .models import Interns, Participant
from .forms import RegistrationForm

# Create your views here.

def index(request):

    meetup = Interns.objects.all()
    return render(request,'meetups/home.html',{'meetup':meetup})

def details(request,intern_slug):
    intern_detail = Interns.objects.get(slug=intern_slug)
    if request.metho == 'GET':
        registration_form = RegistrationForm()
        
    else:
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            Participant = registration_form.save()
    
    return render(request,'meetups/meetup_details.html',{
            'details':intern_detail,
            'form':registration_form
            })