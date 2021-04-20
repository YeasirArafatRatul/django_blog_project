from django import forms
from .models import Person



class AddPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name','last_name','email','gender')



class UserForm(forms.Form):
    first_name = forms.CharField(label="Enter first name",max_length=100)  
    last_name  = forms.CharField(label="Enter last name", max_length = 100)

