from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ReservationForm
from .models import Reservation
from datetime import datetime, time
from django.core.exceptions import ValidationError



@login_required
def reservation_view(request):
    form = ReservationForm(request=request)

    if request.method == 'POST':
        form = ReservationForm(request.POST, request=request)

        if form.is_valid():
            time_value = form.cleaned_data['time']
            date_value = form.cleaned_data['date']
            
            is_weekend = date_value.weekday() >= 5

            if is_weekend:
                start_time = time(8, 0) 
                end_time = time(18, 0)  
            else:
                start_time = time(7, 30)  
                end_time = time(17, 30) 

            if not start_time <= time_value <= end_time:
                form.add_error('time', 'Reservation time is outside the allowed range.')
                return render(request, 'reservations/reserver.html', {'form': form})

            reservation = Reservation(
                user=request.user,
                date=date_value,
                time=time_value,
                num_guests=form.cleaned_data['personnes'],
                reservation_type=form.cleaned_data['type_reservation']
            )
            reservation.save()
            return redirect('booking_list')

    return render(request, 'reservations/reserver.html', {'form': form})    

@login_required
def my_bookings(request):
    reservations=Reservation.objects.filter(user=request.user)
    context={
        "reservations":reservations,
    }
    return render(request, "reservations/my_reservations.html",context)

@login_required
def delete_reservation(request, reservation_id):
    reservation=Reservation.objects.get(user=request.user, id=reservation_id)
    reservation.delete()
    return redirect('booking_list')