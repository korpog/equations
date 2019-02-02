from django.shortcuts import render
from .forms import CreationForm
from .utils import get_determinant


def index(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            num_of_equations = form.cleaned_data['num']
    else:
        form = CreationForm()
    return render(request, 'index.html', {'form': form})


def create_equations(request):
    return render(request, 'results.html', context={'det': get_determinant()})
