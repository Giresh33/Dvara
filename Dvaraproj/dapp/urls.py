from django.shortcuts import render
from django.conf.urls import url
# Create your views here.
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    # url('', RedirectView.as_view(pattern_name='person_changelist'), name='home'),
    url('', views.PersonListView.as_view(), name='person_changelist'),
    url('add/', views.PersonCreateView.as_view(), name='person_add'),
    url('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    url('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]