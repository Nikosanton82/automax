from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation



def main_view(request):
    return render(request, "views/main.html", {"name": "AutoMax"})

def tours_view(request):
    return render(request, 'views/tours.html', {})


def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()

    return render(request, 'views/reservation_form.html', {'form': form})

def reservation_success(request):
    return render(request, 'views/reservation_success.html')


