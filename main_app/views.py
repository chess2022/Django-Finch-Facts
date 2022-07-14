from django.shortcuts import render, redirect
from django.http import HttpResponse
from main_app.forms import SightingForm
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views.generic import ListView, DetailView


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['photo', 'region', 'description']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'


def home(request):
    return HttpResponse('<h1>Home is where the finches are</h1>')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    finches = Finch.objects.order_by('name')
    return render(request, 'finches/index.html', { 'finches': finches })

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', { 
        'finch': finch,
        'sighting_form': sighting_form, 
        })

def add_sighting(request, finch_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)