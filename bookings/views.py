from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Table, Reservation
from .forms import ReservationForm

def home(request):
    """Renders the home page with available tables and booking form."""
    tables = Table.objects.all()
    form = ReservationForm()
    return render(request, 'bookings/home.html', {'tables': tables, 'form': form})

def make_reservation(request):
    """Handles form submission for table bookings."""
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save() # Save the form (automatically creates the Reservation)
            return JsonResponse({'message': 'Reservation successful!'})
        else:
            return JsonResponse({'error': 'Invalid form submission', 'errors': form.errors}, status=400)
        
    return JsonResponse({'error': 'Invalid request'}, status=400)
