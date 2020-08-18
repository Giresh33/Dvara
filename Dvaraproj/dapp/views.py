from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person, Category, Subcategory
from .forms import PersonForm
from django.shortcuts import render

class PersonListView(ListView):
    print('=----------==listviewwwwwww')
    model = Person
    context_object_name = 'person'
    # template_name = "person_form.html"

class PersonCreateView(CreateView):
    print('-=-=-=--=-=======createvieww')
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    print('=-=-=-updateview')
    model = Person
    form_class = PersonForm
    success_url = reverse_lazy('person_changelist')

def load_cities(request):
    country_id = request.GET.get('category')
    cities = Subcategory.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'dapp/city_dropdown_list_options.html', {'cities': cities})