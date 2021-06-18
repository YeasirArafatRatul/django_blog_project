from django.urls import path
from .views import third_party_post_api
from . import views



urlpatterns = [


    path('third-party-post-api/', third_party_post_api,),

       
]


