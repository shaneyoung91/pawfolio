from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {
        'dogs' : dogs
    })