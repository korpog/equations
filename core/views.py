from django.shortcuts import render, redirect
from django.forms import formset_factory
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
    EquationFormSet = formset_factory(EquationForm, extra=num - 1)
    if request.method == 'POST':
        formset = EquationFormSet(request.POST, form_kwargs={'num': num})
        if formset.is_valid():
            return render(request, 'results.html', context={'data': request.POST})
    formset = EquationFormSet(form_kwargs={'num': num})
    return render(request, 'equations.html', context={'formset': formset})


def get_results(request):
    pass
