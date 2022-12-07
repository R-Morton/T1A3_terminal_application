# Create home page where user selects options to choose from
import os
from add_booking import add_booking
def home_page():
    while True:
        os.system('clear')
        print("1 - View today's bookings")
        print("2 - Add a booking")
        print("3 - Edit a booking")
        print("4 - Exit program")
        user_input = int(input("Please select an option: "))
        if user_input == 2:
            os.system('clear')
            add_booking()
        if user_input == 4:
            print("Goodbye!")
            break
home_page()

