import os
from time import sleep
bookings_file = open("src/bookings_list.txt", "a+")
def add_booking():
    first, last = booking_name()
    service, time = booking_time()
    pax_variable = pax()
    new_booking = f"{str(time)} {str(service)} {first} {last} {str(pax_variable)}"
    confirm_booking(new_booking)
    if new_booking == False:
        pass
    else:
        bookings_file.write("\n" + new_booking)
        bookings_file.flush()

def booking_name():
    while True:
        f_name = input("Please enter first name: ")
        if f_name.isspace() == True or f_name == "":
            print("This cannot be left blank")
        else:
            break
    while True:
        l_name = input("Please enter last name: ")
        if l_name.isspace() == True or l_name == "":
            print("This cannot be left blank")
        else:
            break
    return f_name, l_name

def booking_time():
    while True:
        print("1 - Breakfast")
        print("2 - Lunch")
        print("3 - Dinner")
        service = int(input("Please enter a number to select service: "))
        if service == 1:
            while True:
                time = input("Please enter a time between 0700 and 1200: ")
                if int(time.zfill(1)) < 700 or int(time) > 1200:
                    print("Please enter a valid time")
                    continue
                else:
                    break
            break
        if service == 2:
            while True:
                time = int(input("Please enter a time between 1200 and 1530: "))
                if time < 1200 or time > 1530:
                    print("Please enter a valid time")
                    continue
                else:
                    break
            break
        if service == 3:
            while True:
                time = int(input("Please enter a time between 1730 and 2100: "))
                if time < 1730 or time > 2100:
                    print("Please enter a valid time")
                    continue
                else:
                    break
            break
        else:
            print("Please select a valid option")
            continue
    return service, time

def pax():
    while True:
        pax = int(input("How many guests are attending?: "))
        if pax <= 0:
            print("Please enter atleast one or more guests")
            continue
        elif pax >20:
            print("Bookings above 20 must be refered to the functions team")
            continue
        else:
            break
    return pax

def confirm_booking(booking):
    os.system('clear')
    if booking.split()[1] == '1':
        service_name = "Breakfast"
    elif booking.split()[1] == '2':
        service_name = "Lunch"
    elif booking.split()[1] == '3':
        service_name = "Dinner"
    print("Booking details:")
    print(f"Name - {booking.split()[2]} {booking.split()[3]}")
    print(f"Service - {service_name}")
    print(f"Time - {booking.split()[0]}")
    print(f"Number of Guests - {booking.split()[4]}")
    while True:
        add_confirmation = input("Please confirm with 'Y' to add booking or 'N' to cancel: ")
        if add_confirmation.lower() == 'y':
            print("Booking has sucessfully been added")
            sleep(2)
            return booking
        elif add_confirmation.lower() == 'n':
            print("Booking process has been cancelled")
            sleep(2)
            return False
        else:
            print("Please input a valid response")
            continue
