from add_booking import booking_name
from add_booking import booking_time
from add_booking import pax
from add_booking import confirm_booking
from time import sleep
import os
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
        if name_search == line.split()[2] or name_search == line.split()[3]:
            results += 1
            matching_names.append(line)
            print(f"{results} - {line.split()[0]} {line.split()[2]} {line.split()[3]} {line.split()[4]}")
        else:
            continue
    user_input = int(input("Please select from the matches: "))
    count = 1
    for booking in matching_names:
        if user_input == count:
            selected_booking = booking
            os.system('clear')
            print(f'{selected_booking.split()[0]} {selected_booking.split()[2]} {selected_booking.split()[3]} {selected_booking.split()[4]}')
            break
        else:
            count += 1
            continue
    edit_continue = input("Please press 1 to edit or 0 to go back: ")
    while True:
        if edit_continue == '1':
            edit_booking(selected_booking)
        elif edit_continue == '0':
            os.system('clear')
            search_booking()
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
                new_first, new_last = booking_name()
                a = new_booking.replace(new_booking.split()[2], new_first, 1)
                new_booking = a.replace(new_booking.split()[3], new_last, 1)
                count = True
            case "2":
                new_service, new_time = booking_time()
                a = new_booking.replace(new_booking.split()[1], str(new_service), 1)
                new_booking = a.replace(new_booking.split()[0], str(new_time), 1)
                count = True
            case "3":
                print("PAX")
                new_pax = pax()
                a = new_booking.rsplit(new_booking.split()[4], 1)
                new_booking = str(new_pax).join(a)
                count = True
            case "4":
                if count == True:
                    confirm_booking(new_booking)
                    break
                else:
                    print("Invalid")
            case _:
                print("Invalid")
    with open("src/bookings_list.txt", "r") as f:
        lines = f.readlines()
    with open("src/bookings_list.txt", "w") as f:
        for line in lines:
            if line.strip('/n') != booking:
                f.write(line)
        f.write("\n" + new_booking)
    home_page()

