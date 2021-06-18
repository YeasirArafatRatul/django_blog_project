from django.urls import path,include
from .views import  SignUpView, sessions_demo, third_party_post_api, thrid_party_api_view
from . import views


from rest_framework.routers import DefaultRouter
from .views import PersonViewset, PersonModelViewSet, NestedSerializerViewSet, CarsNestedSerializerViewSet, PersonProfileViewSet

# Object of DefaultRouter
router = DefaultRouter()
# router.register('api',PersonViewset, basename='person')
# router.register('',PersonModelViewSet, basename='model-person')
router.register('profile', NestedSerializerViewSet, basename='profile')
router.register('cars', CarsNestedSerializerViewSet, basename='car')
# urlpatterns = router.urls

router.register('all-person-profile', PersonProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),




    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('num-visits/', sessions_demo, name='num-visits'),
    path('set-session/', views.set_session),
    path('get-session/', views.get_session),
    path('delete-session/', views.delete_session),

    path('set-cookie/',views.set_cookie),
    path('get-cookie/',views.get_cookie),
    path('update-cookie/',views.update_cookie),
    path('delete-cookie/', views.delete_cookie),


    path('api/persons/function', views.person_api_view),
    path('api/persons/', views.PersonAPIView.as_view(), name='persons_api'),
    path('api/generic-persons/', views.GenericPersonAPIView.as_view(), name='generic_ersons_api'),


    path('api/create-person/',views.PersonCreateAPIView.as_view()),
    path('api/person-detail/<int:pk>',views.PersonDetailAPIView.as_view()),
    path('api/person-update/<int:pk>',views.PersonUpdateAPIView.as_view()),
    path('api/person-delete/<int:pk>',views.PersonDeleteAPIView.as_view()),

    path('api/person-list-create/<int:pk>',views.PersonListCreateApiView.as_view()),

    path('api/person-update-delete/<int:pk>',views.PersonRetriveUpdateAPIView.as_view()),
    path('api/person-get-delete/<int:pk>',views.PersonRetriveDeleteAPIView.as_view()),
    path('api/person-get-update-delete/<int:pk>',views.PersonRetrieveUpdateDestroyAPIView.as_view()),


    path('api/third-party-api/', thrid_party_api_view,),


    path('api/add-person/', views.AddPersonView.as_view(),),



       
        ]


