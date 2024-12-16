
for booking in bookings:
    if (booking.check_in_date <= get_check_in_date >= booking.check_out_date) and (booking.check_in_date <= get_check_out_date >= booking.check_out_date):
        warn_message = '''
        <br>
        <h2 сlass = "warn-date">Цей час вже зарезервовано</h2>
        <br>
        '''
    elif (booking.check_in_date <= get_check_in_date >= booking.check_out_date) and not(booking.check_in_date <= get_check_out_date >= booking.check_out_date):
        warn_message = '''
        <br>
        <h2 сlass = "warn-date">Виберіть інший час заселення</h2>
        <br>
        '''
    elif (booking.check_in_date <= get_check_out_date >= booking.check_out_date) and not( booking.check_in_date <= get_check_in_date >= booking.check_out_date):
        warn_message = '''
        <br>
        <h2 сlass = "warn-date">Виберіть інший час виселення</h2>
        <br>
        '''
#-------------------------------------------------------------------------------------------------------------------------------------------
elif (booking.check_in_date <= booking_check_in_date <= booking.check_out_date) and not (
        booking.check_in_date <= booking_check_out_date <= booking.check_out_date):
warn_message = '''
    <br>
    <h2 class="warn-date">Виберіть інший час заселення</h2>
    <br>
    '''
print("ЗАСЕЛЕННЯ!!!")
return redirect("book-room-page", room_id=room_id)
elif not (booking.check_in_date <= booking_check_in_date <= booking.check_out_date) and (
        booking.check_in_date <= booking_check_out_date <= booking.check_out_date):
warn_message = '''
    <br>
    <h2 class="warn-date">Виберіть інший час виселення</h2>
    <br>
    '''
print("ВИСЕЛЕННЯ!!!")
return redirect("book-room-page", room_id=room_id)