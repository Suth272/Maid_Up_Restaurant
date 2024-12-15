from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # The home page at '/'
    path('make_reservation/', views.make_reservation, name='make_reservation'),  # Route to handle form submissions
]