from django.contrib import admin
from first_app.models import Person,Car,PersonsProfile,Laptop

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','gender','email',]


class CarAdmin(admin.ModelAdmin):
    list_display = ['name',]  


class PersonProfileAdmin(admin.ModelAdmin):
    list_display = ['username','bio','phone_no']  


class LaptopAdmin(admin.ModelAdmin):
    list_display = ['name','price']  

admin.site.register(Laptop,LaptopAdmin)
# admin.site.register(Car,CarAdmin)
admin.site.register(Person, PersonAdmin)
# admin.site.register(PersonsProfile,PersonProfileAdmin)


from django.contrib.admin import AdminSite

class SecondAdminSite(AdminSite):
    site_header = "Second Admin Page"
    site_title = "Admin Portal 2"
    index_title = "Car & Person Profile Admin"

second_admin_site = SecondAdminSite(name='Second Admin')

second_admin_site.register(Car)
second_admin_site.register(PersonsProfile)
