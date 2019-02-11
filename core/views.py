from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from .forms import CreationForm, EquationForm
from .utils import solve
import numpy as np


def index(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            num_of_equations = form.cleaned_data['num']
            return redirect('equations', num=num_of_equations)
    else:
        form = CreationForm()
    return render(request, 'index.html', {'form': form})


def solve_equations(request, num):
    EquationFormSet = formset_factory(EquationForm, extra=num)
    if request.method == 'POST':
        formset = EquationFormSet(request.POST, form_kwargs={'num': num})
        coefs = np.zeros((num, num), dtype=float)
        b_vals = np.zeros((num), dtype=float)
        if formset.is_valid():
            for i, form in enumerate(formset):
                try:
                    for j in range(num):
                        coefs[i, j] = form.cleaned_data[f'coef_{j + 1}']
                    b_vals[i] = form.cleaned_data['b']
                except (KeyError):
                    return HttpResponseRedirect(reverse('equations', args=(num,)))
            solutions = solve(coefs, b_vals)
            return render(request, 'results.html', context={'solutions': solutions})
    formset = EquationFormSet(form_kwargs={'num': num})
    return render(request, 'equations.html', context={'formset': formset})
