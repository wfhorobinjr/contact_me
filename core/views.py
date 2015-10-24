from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class Home(TemplateView):
  template_name = 'home.html'

class ContactCreateView(CreateView):
  model = Contact
  template_name = "contact/contact_form.html"
  fields = ['title', 'name', 'email', 'message']
  success_url = reverse_lazy('success')

class Success(TemplateView):
  template_name = "success.html"

class AboutMeView(TemplateView):
  template_name = "about_me.html"
# Create your views here.
