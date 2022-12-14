import os
from time import sleep
import phone

def add_booking(): #Declares multiple variables from return values of functions
    bookings_file = open("src/bookings_list.txt", "a+")
    first, last = booking_name()
    phone_num = phone.bookings_phone()
    service, time = booking_time()
    pax_variable = pax()
    new_booking = f"{str(time)} {str(service)} {first} {last} {str(phone_num)} {str(pax_variable)}"
    if confirm_booking(new_booking, False) == False:
        return
    else: #Writes new booking in once all functions passed
        print("Booking has sucessfully been added", flush=True)
        bookings_file.write("\n" + new_booking)
        bookings_file.flush()
        sleep(2)

def booking_name(): #Returns first and last name
    while True:
        f_name = input("Please enter first name: ")
        if name_checker(f_name) == True:
            break
    while True:
        l_name = input("Please enter last name: ")
        if name_checker(l_name) == True:
            break
    os.system('clear')
    return f_name, l_name

def name_checker(name): #Checks name for errors
        if name.isspace() == True or name == "":
                print("This cannot be left blank", flush=True)
                sleep(2)
                os.system('clear')
                return False
        elif len(name.split()) > 1:
                print("Please only enter one name", flush=True)
                sleep(2)
                os.system('clear')
                return False
        else:
            return True

def booking_time(): #Returns service and time
    while True:
        print("1 - Breakfast")
        print("2 - Lunch")
        print("3 - Dinner")
        service = input("Please enter a number to select service: ")
        match service:
            case '1':
                service_range = (800, 1200)
            case '2':
                service_range = (1200, 1530)
            case '3':
                service_range = (1730, 2100)
            case _:
                print("Please enter a valid option", flush=True)
                sleep(2)
                os.system('clear')
                continue
        os.system('clear')
        while True:
            time = input(f"Please enter a time between {service_range[0]} and {service_range[1]}: ")
            if time_checker(time) == False:
                continue
            if time == "" or int(time) < service_range[0] or int(time) > service_range[1]:
                print("Please enter a valid time", flush=True)
                sleep(2)
                os.system('clear')
            elif len(time) <= 999:
                time = time.zfill(1)
                return service, time
            else:
                return service, time

def time_checker(time): #Function that checks time input isnt above 60 minutes for each hour
    count = 1
    if time.isdigit() == False:
        print("Please enter a valid time", flush=True)
        sleep(2)
        os.system('clear')
        return False
    for x in str(time):
        if count == 3:
            if int(x) > 5:
                print("Please enter a valid time", flush=True)
                sleep(2)
                os.system('clear')
                return False
            else:
                return True
        count += 1

def pax(): #PAX is the term used to say how many people are dining in the booking
    while True:
        pax = input("How many guests are attending?: ")
        if pax == "" or int(pax) <= 0:
            print("Please enter atleast one or more guests", flush=True)
            sleep(2)
            os.system('clear')
        elif int(pax) >20:
            print("Bookings above 20 must be refered to the functions team", flush=True)
            sleep(2)
            os.system('clear')
        else:
            os.system('clear')
            break
    return pax

def confirm_booking(booking, edit): #Function to layout all the information for confirmation
    os.system('clear')
    if booking.split()[1] == '1': #If statements to turn the 'service' int into a string to label the service for confirmation
        service_name = "Breakfast"
    elif booking.split()[1] == '2':
        service_name = "Lunch"
    elif booking.split()[1] == '3':
        service_name = "Dinner"
    while True:
        print("Booking details:")
        print(f"Name - {booking.split()[2]} {booking.split()[3]}")
        print(f"Phone Number - {booking.split()[4]}")
        print(f"Service - {service_name}")
        print(f"Time - {booking.split()[0]}")
        print(f"Number of Guests - {booking.split()[5]}")
        if edit == True: #If true, this will skip the rest and we are editing not creating. 
            return
        add_confirmation = input("Please confirm with 'Y' or 'N' to cancel: ")
        if add_confirmation.lower() == 'y':
            return booking
        elif add_confirmation.lower() == 'n':
            print("Booking process has been cancelled", flush=True)
            sleep(2)
            return False
        else:
            print("Please input a valid response", flush=True)
            sleep(2)
            os.system('clear')
            continue
