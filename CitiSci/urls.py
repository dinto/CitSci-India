from django.urls import path
from CitiSci import views

urlpatterns = [
    path('', views.CitiSci, name='index'),
    path('CitSci', views.Cit, name='CitSci'),
    path('tools', views.tools, name='tools'),
    path('projects', views.projects, name='projects'),
    path('training', views.training, name='training'),
    path('bibliography', views.bibliography, name='bibliography'),
]