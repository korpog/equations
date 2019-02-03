from django.shortcuts import render, redirect
from .forms import CreationForm, EquationForm
from .utils import get_determinant


def index(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            num_of_equations = form.cleaned_data['num']
            return redirect('equations', num=num_of_equations)
    else:
        form = CreationForm()
    return render(request, 'index.html', {'form': form})


def create_equations(request, num):
    form = EquationForm(num)
    return render(request, 'equations.html', context={'form': form})

def get_results(request):
    pass
