from django.urls import path
from .views import SignUpView, sessions_demo
from . import views
urlpatterns = [

    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('num-visits/', sessions_demo, name='num-visits'),
    path('set-session/', views.set_session),
    path('get-session/', views.get_session),
    path('delete-session/', views.delete_session),

    path('set-cookie/',views.set_cookie),
    path('get-cookie/',views.get_cookie),
    path('update-cookie/',views.update_cookie),
    path('delete-cookie/', views.delete_cookie),
    ]