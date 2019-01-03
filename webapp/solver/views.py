from django.shortcuts import render
from .computorV1 import computor

def index(request):
	return render(request, 'solver/index.html')

def solver(request):
	return render(request, 'solver/solver.html')

def solution(request):
	return render(request, 'solver/solution.html', {'content' : computor.solve_equ("1 * X^0 = 0 * X^1 + 1 * X^2")})