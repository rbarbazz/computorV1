from django.shortcuts import render
import computor.py

def index(request):
	return render(request, 'solver/index.html')

def solver(request):
	return render(request, 'solver/solver.html')

def solution(request):
	return render(request, 'solver/solution.html', {'content' : computor('1 * X^0 = 0 * X^1')})