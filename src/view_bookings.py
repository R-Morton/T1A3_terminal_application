import os
def view_bookings_menu():
    print("1 - All Services")
    print("2 - Breakfast")
    print("3 - Lunch")
    print("4 - Dinner")
    print("5 - Go back")
    user_input = int(input("Please select a service to view: "))
    if user_input == 1:
        os.system("clear")
        print("All Services -")
        view_file('all')
    elif user_input == 2:
        os.system("clear")
        print("Breakfast bookings -")
        view_file('1')
    elif user_input == 3:
        os.system("clear")
        print("Lunch bookings -")
        view_file('2')
    elif user_input == 4:
        os.system("clear")
        print("Dinner bookings -")
        view_file('3')
    elif user_input == 5:
        pass

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
