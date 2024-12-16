from django.shortcuts import render, redirect
from booking.models import Service, Room, Review, Employe, Payment, Booking, BookingServiceEmploye
from datetime import datetime
from django.utils import timezone
from django.db.models import Q
from auth_system.models import CustomUser


# Create your views here.

def home_page (request):
    return render(
        request,
        template_name="booking/home.html",
    )

def get_rooms(request):
    if request.method == "POST":
        search_room_capacity = request.POST.get("search-room-capacity")
        rooms = Room.objects.filter(capacity = search_room_capacity).all()
    else:
        rooms = Room.objects.all()
    context = {
        "rooms": rooms,
    }
    return render(
        request,
        template_name="booking/rooms.html",
        context=context,
    )
def room_details(request, room_id):
    room = Room.objects.get(id = room_id)
    reviews = Review.objects.filter(room=room).all()
    context = {
        "room": room,
        "reviews": reviews,
    }
    return render(
        request,
        template_name="booking/room_details.html",
        context=context,
    )

def add_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        room_capacity = request.POST.get("room-capacity")
        room_mini_desc = request.POST.get("room-mini-description")
        room_description = request.POST.get("room-description")
        room_price_per_night = request.POST.get("room-price-per-night")
        room_rating = request.POST.get("room-rating")
        room_type = request.POST.get("select-type-room")


        room = Room.objects.create(
            number=room_number,
            capacity=room_capacity,
            mini_description=room_mini_desc,
            description=room_description,
            price_per_night=room_price_per_night,
            rating = room_rating,
            type = room_type
        )
        return redirect("room-details", room_id = room.id)
    else:
        return redirect("/rooms")


def book_room_page(request, room_id):
    room = Room.objects.get(id = room_id)
    warn_message = request.session.pop('warn_message', None)
    context = {
        "room": room,
        'warn_message': warn_message,
    }
    return render(
        request,
        template_name="booking/book-room.html",
        context=context,
    )

def book_room(request, room_id, user_id):
    if request.method == "POST":
        booking_check_in = request.POST.get("booking_check_in_date")
        booking_check_out = request.POST.get("booking_check_out_date")
        payment_method = request.POST.get("payment_method")

        try:
            room = Room.objects.get(id=room_id)
            user = CustomUser.objects.get(id=user_id)
        except Room.DoesNotExist:
            return redirect('room-details', room_id=room_id)
        except CustomUser.DoesNotExist:
            return redirect('login')

        bookings_with_room_id = Booking.objects.filter(room=room).all()

        booking_check_in_date = timezone.make_aware(datetime.strptime(booking_check_in, "%Y-%m-%dT%H:%M"))
        booking_check_out_date = timezone.make_aware(datetime.strptime(booking_check_out, "%Y-%m-%dT%H:%M"))

        for booking in bookings_with_room_id:
            if (booking.check_in_date <= booking_check_in_date <= booking.check_out_date) or (
                    booking.check_in_date <= booking_check_out_date <= booking.check_out_date):
                warn_message = '''
                <br>
                <h2 class="warn-date">Цей час вже зарезервовано!</h2>
                <br>
                '''
                request.session['warn_message'] = warn_message
                return redirect("book-room-page", room_id=room_id)

        nights = (booking_check_out_date - booking_check_in_date).days
        total_cost = room.price_per_night * nights

        booking = Booking.objects.create(
            room=room,
            user=user,
            check_in_date=booking_check_in_date,
            check_out_date=booking_check_out_date,
            total_price=total_cost
        )
        payment = Payment.objects.create(
            user=user,
            booking=booking,
            full_price=total_cost,
            payment_method=payment_method
        )
        return redirect("rooms")
    else:
        return redirect("book-room-page", room_id=room_id)


def add_review(request, room_id, user_id):
    if request.method == "POST":
        review_rating = request.POST.get("review-rating")
        review_comment = request.POST.get("review-comment")

        try:
            room = Room.objects.get(id=room_id)
            user = CustomUser.objects.get(id=user_id)
        except Room.DoesNotExist:
            return redirect('room-details', room_id=room_id)
        except CustomUser.DoesNotExist:
            return redirect('login')

        review = Review.objects.create(
            user=user,
            room=room,
            rating=review_rating,
            comment=review_comment
        )
        return redirect("room-details", room_id=room.id)
    else:
        return redirect("room-details", room_id=room_id)



#def add_service(request, booking_id, service_id):


def user_page(request, user_id):
    user = CustomUser.objects.get(id = user_id)
    bookings = Booking.objects.filter(user=user).all()
    payments = Payment.objects.filter(user=user).all()
    services = Service.objects.all()
    employes = Employe.objects.all()
    context = {
        "bookings": bookings,
        "payments": payments,
        "user": user,
        "services": services,
        "employes": employes,
    }
    return render(
        request,
        template_name="booking/user_page.html",
        context=context
    )

def finish_payment(request, payment_id, user_id):
    if request.method == "POST":
        payment = Payment.objects.get(id = payment_id)
        booking_bsue = payment.booking
        bsue = BookingServiceEmploye.objects.filter(booking = booking_bsue).all()
        bsue.delete()
        payment.booking.delete()
        payment.delete()
        return redirect("user-page", user_id=user_id)
    else:
        return redirect("user-page", user_id=user_id)

def search_room(request):
    if request.method == "POST":
        search_room_number = request.POST.get("search-room-number")
        rooms = Room.objects.filter(capacity__gte=search_room_number).all()
        return render(
            request,
            template_name="booking/rooms.html",
            context={"rooms": rooms}
        )
    else:
        return redirect("rooms")

def add_service_to_booking(request, booking_id, user_id):
    if request.method == "POST":
        service_booking_id = request.POST.get("service-booking")
        employe_booking_id = request.POST.get("employe-booking")

        service = Service.objects.get(id = int(service_booking_id))
        employe = Employe.objects.get(id = int(employe_booking_id))
        booking = Booking.objects.get(id = booking_id)
        user = CustomUser.objects.get(id = user_id)

        bsue = BookingServiceEmploye.objects.create(
            booking =booking,
            service =service,
            user = user,
            employe = employe
        )
        booking.total_price += service.charge
        booking.save()
        payment = Payment.objects.filter(booking=booking).first()
        payment.full_price += service.charge
        payment.save()
        return redirect('user-page', user_id=user_id)
    else:
        return redirect("user-page", user_id=user_id)

def services_booking(request, booking_id):
    booking = Booking.objects.get(id = booking_id)
    bsues = BookingServiceEmploye.objects.filter(booking = booking)

    return render(
        request,
        template_name="booking/booking-services.html",
        context = {"bsues": bsues}
    )


def services_page(request):
    services = Service.objects.all()
    employes = Employe.objects.all()
    context = {
        "services": services,
        "employes": employes
    }
    return render(
        request,
        template_name="booking/services.html",
        context=context
    )











