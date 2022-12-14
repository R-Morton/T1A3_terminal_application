import os
from time import sleep
import view_bookings
import search_edit
import add_bookings

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
            view_bookings.view_bookings_menu()
        case "2":
            os.system('clear')
            add_bookings.add_booking()
        case "3":
            os.system('clear')
            search_edit.search_booking()
        case "4":
            print("Goodbye!", flush=True)
            sleep(2)
            exit()
        case _:
            print("Please input a valid option", flush=True)
            sleep(1)
            os.system('clear')
            continue