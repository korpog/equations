from django.shortcuts import render
from .tasks import get_determinant

def create_equations(request):
    det = get_determinant.delay()
    return render(request, 'results.html', context={'det': det})
