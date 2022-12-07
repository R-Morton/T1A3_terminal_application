import os
bookings_file = open("src/bookings_list.txt", "r")
def view_bookings_menu():
    print("1 - Breakfast")
    print("2 - Lunch")
    print("3 - Dinner")
    print("4 - Go back")
    user_input = int(input("Please select a service to view: "))
    if user_input == 1: 
        view_file()

def view_file():
    lines = bookings_file.readlines()
    for line in lines:
        print(line)

view_bookings_menu()