from django.urls import path
import booking.views as b_views



urlpatterns = [
    path("", b_views.home_page, name="home"),
    path("rooms", b_views.get_rooms, name= "rooms"),
    path("<int:room_id>/", b_views.room_details, name = "room-details"),
    path("add-room/", b_views.add_room, name='add-room'),
    path("book-room-page/<int:room_id>/", b_views.book_room_page, name = 'book-room-page'),
    path("book-room/<int:room_id>/<user_id>/", b_views.book_room, name = "book-room"),
    path("add_review/<int:room_id>/<user_id>/", b_views.add_review, name="add-review"),
    path("user/<user_id>/", b_views.user_page, name = "user-page"),
    path("pay-payment/<payment_id>/<user_id>/", b_views.finish_payment, name = "pay-payment"),
    path("booking-services/<booking_id>/", b_views.services_booking, name = "booking-services"),
    path("add-service-to-booking/<booking_id>/<user_id>/", b_views.add_service_to_booking, name = "add-service-to-booking"),
    path("services", b_views.services_page, name="services"),

]
