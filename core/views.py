from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class Home(TemplateView):
  template_name = 'home.html'

class ContactCreateView(CreateView):
  model = Contact
  template_name = "contact/contact_form.html"
  fields = ['name', 'email', 'message']
  sucess_url = reverse_lazy('home')

# Create your views here.
