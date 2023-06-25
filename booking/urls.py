from django.urls import path
from . import views

urlpatterns = [
    path('',views.reservation_view,name="reserver_table"),
    path('my-bookings/',views.my_bookings,name="booking_list"),
    path('my-bookings/delete/<int:reservation_id>', views.delete_reservation, name="delete_reservation"),

]