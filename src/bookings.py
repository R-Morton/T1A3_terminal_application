# Create home page where user selects options to choose from
import os
import time
from view_bookings import view_bookings_menu
from add_booking import add_booking
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
                pass
            case "4":
                print("Goodbye!")
                time.sleep(2)
                break
            case _:
                print("Please input a valid option")
                time.sleep(1)
                os.system('clear')
                continue
home_page()

