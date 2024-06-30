from django.urls import include, path
from . import views
app_name ='AI_app'
urlpatterns = [
    path('ai',views.Home,name='main'),
    path('ai/heart',views.heart,name='heart'),
    path('ai/diabetes',views.diabetes,name='diabetes'),
]