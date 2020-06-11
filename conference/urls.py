from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.tickets, name="tickets"),
    path('speakers/', views.speakers, name="speakers"),
    path('schedule/', views.schedule, name="schedule"),
   
]