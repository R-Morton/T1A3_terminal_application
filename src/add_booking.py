import os
from time import sleep
bookings_file = open("src/bookings_list.txt", "a+")
def add_booking():
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
    while True:
        print("1 - Breakfast")
        print("2 - Lunch")
        print("3 - Dinner")
        service = int(input("Please enter a number to select service: "))
        if service == 1:
            service_name = "Breakfast"
            while True:
                time = input("Please enter a time between 0700 and 1200: ")
                if int(time.zfill(1)) < 700 or int(time) > 1200:
                    print("Please enter a valid time")
                    continue
                else:
                    break
            break
        if service == 2:
            service_name = "Lunch"
            while True:
                time = int(input("Please enter a time between 1200 and 1530: "))
                if time < 1200 or time > 1530:
                    print("Please enter a valid time")
                    continue
                else:
                    break
            break
        if service == 3:
            service_name = "Dinner"
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
    new_booking = str(str(time) + " " + str(service) + " " + f_name + " " + l_name + " " + str(pax))
    os.system('clear')
    print("Booking details:")
    print(f"Name - {f_name} {l_name}")
    print(f"Service - {service_name}")
    print(f"Time - {time}")
    print(f"Number of Guests - {pax}")
    while True:
        add_confirmation = input("Please confirm with 'Y' to add booking or 'N' to cancel")
        if add_confirmation.lower() == 'y':
            bookings_file.write("\n" + new_booking)
            bookings_file.flush()
            print("Booking has sucessfully been added")
            sleep(2)
            break
        elif add_confirmation.lower() == 'n':
            print("Booking process has been cancelled")
            sleep(2)
            break
        else:
            print("Please input a valid response")
            continue
