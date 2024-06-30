from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('signup', views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('medical',views.medical_sign,name='medical'),
    path('petiant',views.prtiant_sign,name='petiant'),
    path('?/',views.logoutUser,name='logout'),
    path('reception',views.profileReception,name='reception'),
    path('reception/doctor',views.DoctorProfile,name='profile'),
    path('cards',views.cards , name='cards'),
    path('doctor/<slug:slug>/detail',views.Doctor_detail , name='detail'),
    path('cards/<str:sp>',views.special , name='special')
]