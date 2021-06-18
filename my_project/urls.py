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

from first_app.views import PersonDetails, chart,some_data,function_view,AllPersonsView,AddPersonView, AddPersonViewTwo, ChartView
from first_app.views import user_form, all_persons

from django.contrib.auth.views import LoginView, LogoutView
from first_app import views
from keyvalue.views import *

from rest_framework.authtoken.views import obtain_auth_token 
from keyvalue.tasks import time_to_live


from first_app.admin import second_admin_site

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('person/',include('first_app.urls')),

    path('api/', include('authentication.urls')),
    

    path('admin/', admin.site.urls),
    path('second-admin-site/', second_admin_site.urls),


    

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


    path('chart', chart, name='chart'),



#  URLs for KeyValue App
    path('single-pair/<str:key>/', KeyValueRUDApiView.as_view(), name='single-pair'),
    path('all-pairs/', allPairsAPI.as_view(), name='all-pairs'),
    path('create-pair/', addPairView.as_view(), name='create-pair'), 
]
# time_to_live()

admin.site.site_header = "Customized Site Name"
admin.site.site_title = "New Admin Panel"
admin.site.index_title = "Welcome To Admin Panel"