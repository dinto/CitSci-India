from django.urls import path
from CitiSci import views

urlpatterns = [
    path('', views.CitiSci, name='index'),
]