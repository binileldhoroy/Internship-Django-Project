from django.contrib import admin
from .models import Interns, Location, Participant
# Register your models here.

class InternsAdmin(admin.ModelAdmin):
    list_display = ('title','date','location')
    list_filter = ('location','date')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Interns,InternsAdmin)
admin.site.register(Location)
admin.site.register(Participant)
