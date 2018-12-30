from django.shortcuts import render

def index(request):
	return render(request, 'computor/index.html')

def computor(request):
	return render(request, 'computor/computor.html')

def solution(request):
	return render(request, 'computor/solution.html')