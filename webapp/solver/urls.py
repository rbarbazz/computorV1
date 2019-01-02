from django.conf.urls import re_path
from . import views

urlpatterns = [
	re_path(r'^$', views.solver, name='solver'),
	re_path(r'^solution$', views.solution, name='solution'), #debug
]
