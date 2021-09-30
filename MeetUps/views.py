from django.shortcuts import render
from .models import Interns
from .forms import RegistrationForm

# Create your views here.

def index(request):

    meetup = Interns.objects.all()
    return render(request,'meetups/home.html',{'meetup':meetup})

def details(request,intern_slug):
    intern_detail = Interns.objects.get(slug=intern_slug)
    registration_form = RegistrationForm()
    return render(request,'meetups/meetup_details.html',{
        'details':intern_detail,
        'form':registration_form
        })