from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dog
from .forms import ReportCardForm

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
  reportcard_form = ReportCardForm()
  return render(request, 'dogs/detail.html', { 'dog': dog, 'reportcard_form': reportcard_form})

def add_reportcard(request, dog_id):
  form = ReportCardForm(request.POST)
  if form.is_valid():
    new_reportcard = form.save(commit=False)
    new_reportcard.dog_id = dog_id
    new_reportcard.save()
  return redirect('detail', dog_id=dog_id)


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