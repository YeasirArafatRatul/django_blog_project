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



import json

class AllPersonsView(ListView):
    model = Person
    template_name = 'all_persons.html'
    paginate_by = 4
    context_object_name = 'persons'

    def __init__(self):
        print("I am View")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person_json'] = json.dumps(list(Person.objects.values()))
        return context


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def all_persons(request):
    persons = Person.objects.all()
    paginator = Paginator(persons, 4)  # 4 persons in each page
    page = request.GET.get('page')
    print('Page', page)
    try:
        persons_page = paginator.page(page)
        print(persons_page)    
        
    except PageNotAnInteger:
        # If person is not an integer deliver the first page
        persons_page = paginator.page(1)
        print('except', persons_page)

    except EmptyPage:
        # If persons is out of range deliver last page of results
        persons_page = paginator.page(paginator.num_pages)
    return render(request, 'all_persons.html',{'page': page,'persons_page': persons_page,})




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









from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
import json

from .serializers import PersonSerializers
class PersonAPIView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """
        Return a list of all users.
        """
        persons = Person.objects.all()
        serializer = PersonSerializers(persons, many=True)
        return Response(serializer.data)

from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class GenericPersonAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers

    authentication_classes = [ TokenAuthentication ]
    permission_classes = [IsAuthenticated]



from rest_framework.decorators import api_view


@api_view(['GET'])
def person_api_view(request):
    
    persons = Person.objects.all()
    serializer = PersonSerializers(persons, many=True)
    return Response(serializer.data)



from rest_framework.authtoken.models import Token

def create_token(request):
    current_user = request
    check_token = Token.objects.get(user=current_user)

    if check_token == None:
        print('inside condition',check_token)
        token = Token.objects.create(user=request.user)
        print(token)
        return HttpResponse('Token Created')

    print(check_token)
    print(check_token.key)

    return HttpResponse('A Token Is Already Available For This User')





from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        print('created', created)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })



#signals.py



