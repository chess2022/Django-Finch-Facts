from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Finch, Image, Region, Image
from main_app.forms import SightingForm, signUpForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from main_app.forms import signUpForm

import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'finchfacts-cw'

class FinchCreate(LoginRequiredMixin, CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/finches/'

class FinchUpdate(LoginRequiredMixin, UpdateView):
    model = Finch
    fields = ['photo', 'description']

class FinchDelete(LoginRequiredMixin, DeleteView):
    model = Finch
    success_url = '/finches/'
    def get_object(self, queryset=None):
        finch = super(FinchDelete, self).get_object()
        if not finch.user == self.request.user:
            raise Http404
        return finch


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign-up. Please try again'
    form = signUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def finch_index(request):
    finches = Finch.objects.order_by('name')
    return render(request, 'finches/index.html', { 'finches': finches })

@login_required
def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', { 
        'finch': finch,
        'sighting_form': sighting_form,
        })

@login_required
def add_sighting(request, finch_id):
    form = SightingForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)

@login_required
def add_image(request, finch_id):
    image_file = request.FILES.get('image-file', None)
    if image_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + image_file.name[image_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(image_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            image = Image(url=url, finch_id=finch_id)
            image.save()
        except:
            print('An error occurred')
        return redirect('detail', finch_id=finch_id)

@login_required
def assoc_region(request, finch_id, region_id):
    Finch.objects.get(id=finch_id).regions.add(region_id)
    return redirect('detail', finch_id=finch_id)

@login_required
def delete_region(request, finch_id, region_id):
    Finch.objects.get(id=finch_id).regions.remove(region_id)
    return redirect('detail', finch_id=finch_id)

class RegionList(LoginRequiredMixin, ListView):
    model = Region

class RegionDetail(LoginRequiredMixin, DetailView):
    model = Region

class RegionCreate(LoginRequiredMixin, CreateView):
    model = Region
    fields = '__all__'

class RegionUpdate(LoginRequiredMixin, UpdateView):
    model = Region
    fields = '__all__'

class RegionDelete(LoginRequiredMixin, DeleteView):
    model = Region
    success_url = '/regions/'

