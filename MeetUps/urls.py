from django.urls import path
from . import views
urlpatterns = [
    path('meetups/',views.index,name='meetups'),
    path('meetups/details/<slug:intern_slug>/confirm-registration',views.ConfirmReg,name='confirm-registration'),
    path('meetups/details/<slug:intern_slug>',views.details,name='intern-detail'),
]