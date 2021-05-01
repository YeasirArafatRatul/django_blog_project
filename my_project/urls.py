"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from first_app.views import PersonDetails,some_data,function_view,AllPersonsView,AddPersonView, AddPersonViewTwo
from first_app.views import user_form, all_persons

from django.contrib.auth.views import LoginView, LogoutView
from first_app import views


from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/',include('first_app.urls')),
    

    path('admin/', admin.site.urls),
    path('person/<int:pk>/', PersonDetails.as_view(), name='person-detail-view'),
    # path('all-persons/', AllPersonsView.as_view(),name='all-persons'),

    path('func-all-persons/', all_persons,name='all-persons'),
    path('add-person/', AddPersonView.as_view(), name='add-person'),
        path('add-person-two/', AddPersonViewTwo.as_view(), name='add-person'),

    path('data/', some_data),
    path('function-view/<int:person_id>', function_view, name='function-view'),


    path('user-form', user_form, name='user-form'),

    path('create-token/', views.create_token,name='create_token'),

    path('auth-token/', views.CustomAuthToken.as_view(),name='auth_token'),

    path('gettoken/', obtain_auth_token, name='api_token_auth'),

]
