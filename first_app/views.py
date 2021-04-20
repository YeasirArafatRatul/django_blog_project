from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.dates import DayArchiveView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView

from .models import Person, Car
# Create your views here.


class PersonDetails(DetailView):
    model = Person
    template_name = 'details.html'
    
    def get_context_data(self, **kwargs):
        print(super().get_context_data(**kwargs))
        # Call the base implementation(from parent class) first to get a context
        context = super().get_context_data(**kwargs)
        print('Type of context', type(context))
        
        # Add a QuerySet in the 'context' of the cars owned by this person
        context['cars'] = Car.objects.filter(owner=self.kwargs['pk'])
        print(type(context['cars']))
        for i in context:
            print(context[i])
        return context



class AllPersonsView(ListView):
    model = Person
    template_name = 'persons.html'
    context_object_name = 'persons'

    def __init__(self):
        print("I am View")


from .forms import AddPersonForm
class AddPersonView(CreateView):
    form_class = AddPersonForm
    template_name = 'add-person.html'
    



from first_app.forms import UserForm  
class AddPersonViewTwo(FormView):
    form_class = UserForm
    template_name = 'add-person.html'
    success_url = '/all-persons'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # created a person object
        obj = Person()
         # clean data from 'form' and assign them into objects attributes
        obj.first_name = form.cleaned_data['first_name']
        obj.last_name = form.cleaned_data['last_name']
        #finally save the object in db
        obj.save()
        print('Object Saved')
        return HttpResponse("Object Saved")

        # return render(request,"user-form.html",{'form':form})  

        # return super().form_valid(form)


	  
def user_form(request):  
    form = UserForm(request.POST)

    if request.method == 'POST':
        # created a person object
        obj = Person()

        if form.is_valid():
            # clean data from 'form' and assign them into objects attributes
            obj.first_name = form.cleaned_data['first_name']
            obj.last_name = form.cleaned_data['last_name']
            #finally save the object in db
            obj.save()
            print('Object Saved')
            return HttpResponse("Object Saved")

    return render(request,"user-form.html",{'form':form})  


def some_data(request):
    # Get the User of a given car 
    # owner_id = Car.objects.get(name ='BMW').person.name
    # print(owner_id)

    # Get All Owners of a given Car 
    car1 = Car.objects.get(name = 'BMW')
    owners_of_a_specific_car= car1.owner.all()

    print(owners_of_a_specific_car)

    #Get all the Cars of a specific Person (One Way)
    person1 = Person.objects.get(first_name='Zaira')
    cars_of_person1 = person1.car_set.all()
    print(cars_of_person1)

    # Get Cars that belong to the owner 'Zaira' (Another Way)
    owners_all_cars = Car.objects.filter(owner__first_name='Zaira')
    print("Zaira's all cars: ",owners_all_cars)


    person1 = Person.objects.get(first_name='Zaira')
    persons_phone_no = person1.personsprofile.phone_no
  
    print(persons_phone_no)

    return None
    


def function_view(request,person_id):
    person_object = Person.objects.get(id=person_id)

    context = {
        'person':person_object,
    }
    return render(request, 'new_template.html',context)

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('login') 



# from django.contrib.auth import authenticate

# user = authenticate(username='new_user', password='mypassword1234')
# if user is not None:
#     # the password verified for the user
#     if user.is_active:
#         print("User is valid, active and authenticated")
#     else:
#         print("The password is valid, but the account has been disabled!")
# else:
#     # the authentication system was unable to verify the username and password
#     print("The username and password were incorrect.")



def sessions_demo(request):

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

   
    return HttpResponse(num_visits)


def set_session (request):
    request.session['username'] = 'ratul'
    request.session['email'] = 'arafat@gmail.com'


    persons = Person.objects.filter(gender='Female')
    for person in persons:
        request.session[str(person.id)] = person.full_name

    return HttpResponse("Session Set")  


def get_session(request):

    name = request.session['username']
    print(name)
    email = request.session['email']
    print(email)
    all_persons = request.session.session_key
    return HttpResponse(all_persons) 

def delete_session(request):
    # del request.session['username']
    #get the name after deleting if not avaiable get() will show none
    # name = request.session.get('username')
    request.session.clear()
    return HttpResponse('Session Cleaned')





def set_cookie(request):
    response = render(request,'cookies/set_cookies.html')
    response.set_cookie('name','arafat')
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    context = {
        'name':name,
    }
    return render(request,'cookies/get_cookies.html',context )


def update_cookie(request):
    response = render(request,'cookies/update_cookies.html')
    response.set_cookie('name','arafatratul')
    return response



def delete_cookie(request):
    response = render(request,'cookies/update_cookies.html')
    response.delete_cookie('name')
    return response
