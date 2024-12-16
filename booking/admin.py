from django.contrib import admin
from booking.models import Room, Review, Service, Payment, Employe, Booking
# Register your models here.

admin.site.register(Room)
admin.site.register(Review)
admin.site.register(Service)
admin.site.register(Payment)
admin.site.register(Employe)
admin.site.register(Booking)
