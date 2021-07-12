from django.db import models
from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Snack

# Create your views here.

class SnackList(ListView):
    template_name = 'snacklist.html'
    model = Snack


class SnackDetail(DetailView):
    template_name = 'snackdetail.html'
    model = Snack
