from django.urls import path
from . import views
urlpatterns = [path('homepage/',views.homeview,name="homepage"),
               path('work/',views.workview,name='work'),path('projects/',views.projectview,name='projects'),
               path('contact/',views.contactview,name='contact'),path('education/',views.educationview,name='education')]