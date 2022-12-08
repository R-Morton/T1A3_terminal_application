import os
bookings_file = open("src/bookings_list.txt", "r")
def view_bookings_menu():
    print("1 - Breakfast")
    print("2 - Lunch")
    print("3 - Dinner")
    print("4 - Go back")
    user_input = int(input("Please select a service to view: "))
    if user_input == 1:
        os.system("clear")
        print("Breakfast bookings -")
        view_file('1')

def view_file(service):
    for line in bookings_file.readlines():
        if line.split()[1] == service:
            print(line)
        else:
            continue
        



view_bookings_menu()