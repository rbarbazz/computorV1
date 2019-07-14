from django.urls import include, path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.solver, name='solver'),
]
