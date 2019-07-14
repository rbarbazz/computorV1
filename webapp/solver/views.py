from django.shortcuts import render
from django.http import HttpResponseRedirect
from .computorV1 import computor
from .forms import EquForm


def index(request):
    return render(request, 'solver/index.html')


def solver(request):
    if request.method == 'POST':
        form = EquForm(request.POST)
        if form.is_valid():
            solution = computor.solve_equ(form.cleaned_data['equation'])
            solution = solution.split('\n')
            return render(
                request,
                'solver/solution.html',
                {'content': solution}
            )
    else:
        form = EquForm()
    return render(request, 'solver/solver.html', {'form': form})
