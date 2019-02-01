from django.shortcuts import render
from .utils import get_determinant

def create_equations(request):
    det = get_determinant()
    return render(request, 'results.html', context={'det': det})
