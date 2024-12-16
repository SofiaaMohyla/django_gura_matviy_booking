from django.db import models
from auth_system.models import CustomUser

# Create your models here.

class Room(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    mini_description = models.CharField(max_length=150, null =True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=256, default="none")

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="rooms_booking")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="users_booking")
    booking_date = models.DateTimeField(auto_now_add=True)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.booking_date} - {self.total_price}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["booking_date"]

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_payment")
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="bookings_payment")
    payment_date = models.DateTimeField(auto_now_add=True)
    full_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.payment_date} - {self.payment_method}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ["payment_date"]

class Employe(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=256)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"

    class Meta:
        verbose_name = "Employe"
        verbose_name_plural = "Employes"
        ordering = ["first_name"]

class Service(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    charge = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.charge}"

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["name"]

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="uses_review")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="rooms_review")
    review_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.review_date}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ["rating"]

class BookingServiceEmploye(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.booking.id} - {self.service.id} - {self.employe.first_name}"

    class Meta:
        verbose_name = "BookingService"
        verbose_name_plural = "BookingServices"
        ordering = ["booking"]











