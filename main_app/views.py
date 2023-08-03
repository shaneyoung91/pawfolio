import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Dog, Treat, Photo, ReportCard
from .forms import ReportCardForm, TreatForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


@login_required
def dogs_index(request):
    dogs = Dog.objects.filter(user=request.user)
    return render(request, 'dogs/index.html', {
        'dogs' : dogs
    })


@login_required
def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  id_list = dog.treats.all().values_list('id')
  treats_dog_doesnt_have = Treat.objects.exclude(id__in=id_list)
  reportcard_form = ReportCardForm()
  return render(request, 'dogs/detail.html', {
    'dog': dog, 'reportcard_form': reportcard_form,
    'treats': treats_dog_doesnt_have
    })

def add_reportcard(request, dog_id):
  form = ReportCardForm(request.POST)
  if form.is_valid():
    new_reportcard = form.save(commit=False)
    new_reportcard.dog_id = dog_id
    new_reportcard.save()
  return redirect('detail', dog_id=dog_id)

@login_required
def reportcard_detail(request, dog_id, reportcard_id):
  dog = Dog.objects.get(id=dog_id)
  reportcard = ReportCard.objects.get(id=reportcard_id)
  return render(request, 'dogs/reportcard_detail.html', {
    'reportcard': reportcard, 
    'dog': dog
    })


class ReportCardUpdate(LoginRequiredMixin, UpdateView):
  model = ReportCard
  fields = ['date', 'behavior', 'summary', 'fed', 'grade']
  template_name = 'dogs/reportcard_form.html'

  def get_success_url(self):
        return reverse('detail', args=[str(self.kwargs['pk'])])

  def get_object(self, queryset=None):
        # Get the dog's primary key from the URL
        dog_pk = self.kwargs.get('pk')

        # Get the reportcard_id from the URL
        reportcard_id = self.kwargs.get('reportcard_id')

        # Retrieve the specific ReportCard instance to update
        reportcard = ReportCard.objects.get(id=reportcard_id, dog__id=dog_pk)
        return reportcard

  def form_valid(self, form):
        # Save the form and update the ReportCard instance
        reportcard = form.save()
        return super().form_valid(form)


class ReportCardDelete(LoginRequiredMixin, DeleteView):
  model = ReportCard
  template_name = 'dogs/reportcard_confirm_delete.html'
  
  def get_success_url(self):
    return reverse('detail', kwargs={'dog_id': self.kwargs['pk']})
  
  def get_object(self, queryset=None):
        # Get the dog's primary key from the URL
        dog_pk = self.kwargs.get('pk')

        # Get the reportcard_id from the URL
        reportcard_id = self.kwargs.get('reportcard_id')

        # Retrieve the specific ReportCard instance to update
        reportcard = ReportCard.objects.get(id=reportcard_id, dog__id=dog_pk)
        return reportcard
  
  def get_context_data(self, **kwargs):
    # Use super function to access and call methods of the parent class (DeleteView)
    # This ensures we can add customizations to the context without overriding or negating
      # the default behavior of the parent class (DeleteView)
    context = super().get_context_data(**kwargs)
    # Retrieve the correct Dog instance
    context['dog'] = Dog.objects.get(pk=self.kwargs['pk'])  
    return context


class DogCreate(LoginRequiredMixin, CreateView):
  model = Dog
  fields = ['name', 'breed', 'age', 'weight', 'diet', 'vaccinated']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class DogUpdate(LoginRequiredMixin, UpdateView):
  model = Dog
  fields = ['breed', 'age', 'weight', 'diet', 'vaccinated']


class DogDelete(LoginRequiredMixin, DeleteView):
  model = Dog
  success_url = '/dogs'


class TreatList(LoginRequiredMixin, ListView): 
  model = Treat
  

# CIRCLE BACK - ADDING DOG TREAT ON DOG INDEX PAGE
class TreatCreate(LoginRequiredMixin, CreateView):
  model = Treat
# ----------------------


class TreatUpdate(UpdateView):
  model = Treat
  fields = '__all__'


class TreatDelete(DeleteView):
  model = Treat
  success_url = '/treats'


@login_required
def assoc_treat(request, dog_id, treat_id):
    Dog.objects.get(id=dog_id).treats.add(treat_id)
    return redirect('detail', dog_id=dog_id)  


@login_required
def unassoc_treat(request, dog_id, treat_id):
    Dog.objects.get(id=dog_id).treats.remove(treat_id)
    return redirect('detail', dog_id=dog_id)  


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def add_photo(request, dog_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, dog_id=dog_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
    return redirect('detail', dog_id=dog_id)