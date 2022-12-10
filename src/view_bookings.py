import os
from time import sleep
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
                break
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
        if line.split()[1] == service or service == "all":
            print(f"{line.split()[0]} - {line.split()[2]} {line.split()[3]} - {line.split()[4]}pax")
            covers += int(line.split()[4])
        else:
            continue
    print(f"Total covers - {covers}")
    input("Press enter to go back")
    os.system("clear")
    view_bookings_menu()
