from django.contrib import admin
from first_app.models import Person,Car,PersonsProfile

class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name','gender','email',]


class CarAdmin(admin.ModelAdmin):
    list_display = ['name',]  


class PersonProfileAdmin(admin.ModelAdmin):
    list_display = ['username','bio','phone_no']  



admin.site.register(Car,CarAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(PersonsProfile,PersonProfileAdmin)