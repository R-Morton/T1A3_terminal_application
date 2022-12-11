# Create home page where user selects options to choose from
import os
from time import sleep
def home_page():
    while True:
        os.system('clear')
        print("1 - View today's bookings")
        print("2 - Add a booking")
        print("3 - Search/Edit a booking")
        print("4 - Exit program")
        user_input = input("Please select an option: ")
        match user_input:
            case "1":
                os.system('clear')
                view_bookings_menu()
            case "2":
                os.system('clear')
                add_booking()
            case "3":
                os.system('clear')
                search_booking()
            case "4":
                print("Goodbye!")
                sleep(2)
                break
            case _:
                print("Please input a valid option")
                sleep(1)
                os.system('clear')
                continue

def add_booking():
    bookings_file = open("src/bookings_list.txt", "a+")
    first, last = booking_name()
    service, time = booking_time()
    pax_variable = pax()
    new_booking = f"{str(time)} {str(service)} {first} {last} {str(pax_variable)}"
    confirm_booking(new_booking, False)
    if new_booking == False:
        pass
    else:
        bookings_file.write("\n" + new_booking)
        bookings_file.flush()
        print("Booking has sucessfully been added")
        sleep(3)

def booking_name():
    while True:
        f_name = input("Please enter first name: ")
        if f_name.isspace() == True or f_name == "":
            print("This cannot be left blank")
            sleep(2)
            os.system('clear')
        elif len(f_name.split()) > 1:
            print("Please only enter one name")
            sleep(2)
            os.system('clear')
        else:
            break
    while True:
        l_name = input("Please enter last name: ")
        if l_name.isspace() == True or l_name == "":
            print("This cannot be left blank")
            sleep(2)
            os.system('clear')
        elif len(l_name.split()) > 1:
            print("Please only enter one name")
            sleep(2)
            os.system('clear')
        else:
            break
    os.system('clear')
    return f_name, l_name

def booking_time():
    while True:
        print("1 - Breakfast")
        print("2 - Lunch")
        print("3 - Dinner")
        service = input("Please enter a number to select service: ")
        if service == '1':
            os.system('clear')
            while True:
                time = input("Please enter a time between 0700 and 1200: ")
                if time_checker(time) == False:
                    continue
                elif int(time.zfill(1)) < 700 or int(time) > 1200:
                    print("Please enter a valid time")
                    sleep(2)
                    os.system('clear')
                else:
                    os.system('clear')
                    break
            break
        elif service == '2':
            os.system('clear')
            while True:
                time = int(input("Please enter a time between 1200 and 1530: "))
                sleep(2)
                if time < 1200 or time > 1530:
                    print("Please enter a valid time")
                    sleep(2)
                    os.system('clear')
                else:
                    os.system('clear')
                    break
            break
        elif service == '3':
            os.system('clear')
            while True:
                time = int(input("Please enter a time between 1730 and 2100: "))
                if time < 1730 or time > 2100:
                    print("Please enter a valid time")
                    sleep(2)
                    os.system('clear')
                else:
                    os.system('clear')
                    break
            os.system('clear')
            break
        else:
            print("Please select a valid option")
            sleep(2)
            os.system('clear')
            continue
    return service, time

def time_checker(time):
    count = 1
    for x in str(time):
        if count == 3:
            if int(x) > 5:
                print("Please enter a valid time")
                sleep(2)
                os.system('clear')
                return False
            else:
                return True
        count += 1

def pax():
    while True:
        pax = int(input("How many guests are attending?: "))
        if pax <= 0:
            print("Please enter atleast one or more guests")
            sleep(2)
            os.system('clear')
        elif pax >20:
            print("Bookings above 20 must be refered to the functions team")
            sleep(2)
            os.system('clear')
        else:
            os.system('clear')
            break
    return pax

def confirm_booking(booking, edit):
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
    if edit == True:
        return
    while True:
        add_confirmation = input("Please confirm with 'Y' to add booking or 'N' to cancel: ")
        if add_confirmation.lower() == 'y':
            return booking
        elif add_confirmation.lower() == 'n':
            print("Booking process has been cancelled")
            sleep(2)
            return False
        else:
            print("Please input a valid response")
            continue

def view_bookings_menu():
    while True:
        print("1 - All Services")
        print("2 - Breakfast")
        print("3 - Lunch")
        print("4 - Dinner")
        print("5 - Go back")
        user_input = input("Please select a service to view: ")
        match user_input:
            case '1':
                os.system("clear")
                print("All Services -")
                view_file('all')
            case '2':
                os.system("clear")
                print("Breakfast bookings -")
                view_file('1')
            case '3':
                os.system("clear")
                print("Lunch bookings -")
                view_file('2')
            case '4':
                os.system("clear")
                print("Dinner bookings -")
                view_file('3')
            case '5':
                home_page()
            case _:
                print("Please input a valid option")
                sleep(1)
                os.system('clear')
                continue


def view_file(service):
    bookings_file = open("src/bookings_list.txt", "r")
    reservations = bookings_file.readlines()
    reservations.sort()
    covers = 0
    for line in reservations:
        if line.strip() == "":
            continue
        elif line.split()[1] == service or service == "all":
            print(f"{line.split()[0]} - {line.split()[2]} {line.split()[3]} - {line.split()[4]}pax")
            covers += int(line.split()[4])
        else:
            continue
    print(f"Total covers - {covers}")
    input("Press enter to go back")
    os.system("clear")
    view_bookings_menu()

def search_booking():
    bookings_file = open("src/bookings_list.txt", "r")
    matching_names = []
    results = 0
    while True:
        name_search = input("Please type the first or last name of the customer: ")
        if name_search.isspace() == True or name_search == "":
            print("Please enter a name")
            sleep(2)
            os.system("clear")
        else:
            os.system("clear")
            break
    for line in bookings_file.readlines():
        lower_line = line.lower()
        if line.strip() == "":
            continue
        elif name_search.lower() == lower_line.split()[2] or name_search.lower() == lower_line.split()[3]:
            results += 1
            matching_names.append(line)
            print(f"{results} - {line.split()[0]} {line.split()[2]} {line.split()[3]} {line.split()[4]}pax")
        else:
            continue
    user_input = int(input("Please select from the matches: "))
    count = 1
    for booking in matching_names:
        if user_input == count:
            selected_booking = booking
            os.system('clear')
            confirm_booking(booking, True)
            break
        else:
            count += 1
            continue
    edit_continue = input("Please press 1 to edit or 0 to go back: ")
    while True:
        if edit_continue == '1':
            os.system('clear')
            edit_booking(selected_booking)
        elif edit_continue == '0':
            os.system('clear')
            home_page()
        else:
            print('Please enter a valid option')
            sleep(2)
            os.system('clear')
            continue




def edit_booking(booking):
    new_booking = booking
    count = False
    while True:
        print("1 - Name")
        print("2 - Time")
        print("3 - PAX")
        if count == True:
            print("4 - Finished with changes")
        user_input = input("What would you like to change? ")
        match user_input:
            case "1":
                os.system('clear')
                new_first, new_last = booking_name()
                a = new_booking.replace(new_booking.split()[2], new_first, 1)
                new_booking = a.replace(new_booking.split()[3], new_last, 1)
                count = True
            case "2":
                os.system('clear')
                new_service, new_time = booking_time()
                a = new_booking.replace(new_booking.split()[1], str(new_service), 1)
                new_booking = a.replace(new_booking.split()[0], str(new_time), 1)
                count = True
            case "3":
                os.system('clear')
                new_pax = pax()
                a = new_booking.rsplit(new_booking.split()[4], 1)
                new_booking = str(new_pax).join(a)
                count = True
            case "4":
                if count == True:
                    os.system('clear')
                    confirm_booking(new_booking, False)
                    break
                else:
                    print("Please select a valid option")
                    sleep(2)
                    os.system('clear')
            case _:
                print("Please select a valid option")
                sleep(2)
                os.system('clear')

    with open("src/bookings_list.txt", "r") as f:
        lines = f.readlines()
    with open("src/bookings_list.txt", "w") as f:
        for line in lines:
            if line != booking:
                f.write(line)
        f.write("\n" + new_booking)
        print("Your booking has successfully been edited")
        sleep(3)
    home_page()

home_page()
