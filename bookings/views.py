from django.shortcuts import render, redirect
from .models import Table, Reservation
from .forms import ReservationForm
from django.http import JsonResponse

def home(request):
    """Renders the home page with available tables and booking form."""
    tables = Table.objects.all()
    form = ReservationForm()
    return render(request, 'bookings/home.html', {'tables': tables, 'form': form})

def make_reservation(request):
    """Handles reservation form submission."""
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form (automatically creates the Reservation)
            return JsonResponse({'message': 'Reservation successful!'})
        else:
            return JsonResponse({'error': 'Invalid form submission', 'errors': form.errors}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
