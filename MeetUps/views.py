from django.shortcuts import redirect, render
from .models import Interns, Participant
from .forms import RegistrationForm

# Create your views here.

def index(request):

    meetup = Interns.objects.all()
    return render(request,'meetups/home.html',{'meetup':meetup})

def details(request,intern_slug):
    intern_detail = Interns.objects.get(slug=intern_slug)
    registration_form = RegistrationForm()
        
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user_email = registration_form.cleaned_data['email']
            participant, _ = Participant.objects.get_or_create(email=user_email)
            intern_detail.participants.add(participant)
            return redirect('confirm-registration',intern_slug=intern_slug)

    
    return render(request,'meetups/meetup_details.html',{
            'details':intern_detail,
            'form':registration_form
            })

def ConfirmReg(request,intern_slug):
    organizer_email = Interns.objects.get(slug=intern_slug)
    return render(request,'meetups/confirm_registration.html',{'organizer_email':organizer_email})