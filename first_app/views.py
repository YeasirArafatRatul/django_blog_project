import re
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.dates import DayArchiveView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from rest_framework.routers import DefaultRouter

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

from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

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



# CRUD OPERATION
from rest_framework.generics import ( 
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView,
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView, 
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import PersonSerializers 
from authentication.api.customauth import CustomAuthetication
# PARTIAL UPDATE


class PersonCreateAPIView(CreateAPIView):
    serializer_class = PersonSerializers
    authentication_classes = [CustomAuthetication]
    permission_classes = [IsAuthenticated]



class PersonDetailAPIView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    authentication_classes = [CustomAuthetication]
    permission_classes = [IsAuthenticated]




class PersonUpdateAPIView(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers



class PersonDeleteAPIView(DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers


class PersonRetriveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers



class PersonRetriveDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers


class PersonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers



class PersonListCreateApiView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers




from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class PersonViewset(viewsets.ViewSet):
    queryset = Person.objects.all()
    permission_classes = [IsAuthenticated]


    def list(self, request):
        """
        This will return list of objects.
        """
        serializer_class = PersonSerializers(self.queryset, many=True)
        return Response(serializer_class.data)


    def create(self, request):
        """
        This will create an endpoint for POST request.
        """
        serializer = PersonSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
       
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        """
        Returns a single object
        """
        person = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PersonSerializers(person)
        return Response(serializer_class.data)


    def update(self, request, pk):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializers(person, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def partial_update(self, request,pk):
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializers(person, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def destroy(self, request,pk):
        person = Person.objects.get(pk=pk)
        person.delete()




from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class PersonModelViewSet(ModelViewSet):
    serializer_class = PersonSerializers
    queryset = Person.objects.all()

    # serializer_class = PersonSerializers



class NestedSerializerViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers




class CarsNestedSerializerViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


    def create(self, request, *args,**kwargs):
        data = request.data
        print(data)
        new_car = Car.objects.create(name = data['name'],price=data['price'])
        new_car.save()

        # data['owner'] & is a dicationary owner is a nested dictionary
        for owner in data['owner']:
            print(type(owner))
            print(owner)
            car_owner = Person.objects.get(id=owner['id'])
            new_car.owner.add(car_owner)

        serializer = CarSerializer(new_car)

        return Response(serializer.data)



from .serializers import OneToOnePersonSeializer

class PersonProfileViewSet(viewsets.ModelViewSet):
    serializer_class = OneToOnePersonSeializer
    queryset = PersonsProfile.objects.all()


from rest_framework import status

class AddPersonView(APIView):

    def get(self, request, format=None):
        person = Person.objects.all()
        serializer = PersonSerializers(person, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# THIRD PARTY API

import requests
import json
from requests.exceptions import ConnectionError

def thrid_party_api_view(request):
    api_request = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(api_request)

    try: 
        posts = json.loads(api_request.content)[:5]
        print(posts)
    except:
        posts = 'Not found'

    return render(request, 'third_party_api.html', {'posts':posts})



def third_party_post_api(request):
    if request.method == 'POST':
        form = AddPersonForm(request.POST)
        data = form.data
        print(data)
        url = 'http://127.0.0.1/api/add-person'
        api = requests.post(url=url,data=data)
        print(api)

        try:
            response = json.loads(api.text)
            # print(response)
        except ConnectionError as e:
            # print(e)
            response = None
    else:
        form = AddPersonForm()
    
    return render(request, 'add-person.html', {'form':form})


from django.views.generic.base import View

class ChartView(View):
    # queryset = Person.objects.all()
    # serializer_class = PersonSerializers


    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html', {})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):

        data = {
            "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "data": [12, 19, 3, 5, 2, 3, 10],
        }   

        return Response(data)


def chart(request):

    males = Person.objects.filter(gender='Male').count()
    females = Person.objects.filter(gender='Female').count()
    males_and_females = [females, males]


    labels  = Person.objects.values('gender').distinct()
    
    genders = []
    for label in labels :
        genders.append(label['gender'])


    context = {
        'genders':genders,
        'males_and_females':males_and_females,


    }
    return render(request, 'chart.html', context)