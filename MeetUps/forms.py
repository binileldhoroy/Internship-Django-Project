from django import forms
from django.db import models
from django.db.models import fields
from django import forms
from .models import Participant

class  RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your Email')
    