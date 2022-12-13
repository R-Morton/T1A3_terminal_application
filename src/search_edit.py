import add_bookings
from time import sleep
import os

def search_booking(): #Function for searching for a customer before editing
    bookings_file = open("src/bookings_list.txt", "r")
    matching_names = []
    results = 0
    while True:
        name_search = input("Please enter the name of a customer: ")
        if name_search.isspace() == True or name_search == "": #stops user from entering no name
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
        elif name_search.lower() == lower_line.split()[2] or name_search.lower() == lower_line.split()[3] or name_search.lower() == f'{lower_line.split()[2]} {lower_line.split()[3]}': #Checks on each iteration if any name from input matches
            results += 1
            matching_names.append(line) #any matches getting added to list
            print(f"{results} - {line.split()[0]} {line.split()[2]} {line.split()[3]} {line.split()[4]}pax")
        else:
            continue
    if not matching_names:
        print("No matches found")
        sleep(2)
        search_booking()
    user_input = int(input("Please select from the matches: "))
    count = 1
    for booking in matching_names:
        if user_input == count: #Iterates and selects the correct booking the user entered
            selected_booking = booking
            os.system('clear')
            add_bookings.confirm_booking(booking, True) #Using confirm booking function to display the full customer booking details
            break
        else:
            count += 1
            continue
    edit_continue = input("Please press 1 to edit or 0 to go back: ")
    while True:
        if edit_continue == '1':
            os.system('clear')
            edit_booking(selected_booking)
            break
        elif edit_continue == '0':
            os.system('clear')
            break
        else:
            print('Please enter a valid option')
            sleep(2)
            os.system('clear')
            continue


def edit_booking(booking): #Function for editing bookings
    new_booking = booking
    count = False
    delete = False
    while True:
        print("1 - Name")
        print("2 - Time")
        print("3 - PAX")
        print("4 - Delete booking")
        print("5 - Cancel")
        if count == True:
            print("6 - Finished with changes") #This only shows up after editing atleast one variable in the booking
        user_input = input("What would you like to change? ")
        match user_input:
            case "1": #Using name function to edit name
                os.system('clear')
                new_first, new_last = add_bookings.booking_name()
                a = new_booking.replace(new_booking.split()[2], new_first, 1)
                new_booking = a.replace(new_booking.split()[3], new_last, 1)
                count = True
            case "2": #Using time function to edit time
                os.system('clear')
                new_service, new_time = add_bookings.booking_time()
                a = new_booking.replace(new_booking.split()[1], str(new_service), 1)
                new_booking = a.replace(new_booking.split()[0], str(new_time), 1)
                count = True
            case "3": #Using PAX function to edit PAX (amount of people for booking)
                os.system('clear')
                new_pax = add_bookings.pax()
                a = new_booking.rsplit(new_booking.split()[4], 1)
                new_booking = str(new_pax).join(a)
                count = True
            case "4": #Delete function
                os.system('clear')
                check = input("Press enter to confirm you want to delete or press 0 to cancel")
                if check == "0":
                    continue
                else:
                    delete = True 
                    break
            case "5":
                os.system('clear')
                print("Changes have been cancelled")
                sleep(2)
                break
            case "6":
                if count == True:
                    os.system('clear')
                    add_bookings.confirm_booking(new_booking, False) #Calls confirm function to see details again after making changes
                    break
                else:
                    print("Please select a valid option")
                    sleep(2)
                    os.system('clear')
            case _:
                print("Please select a valid option")
                sleep(2)
                os.system('clear')
    if int(user_input) != 5:
        with open("src/bookings_list.txt", "r") as f: #Reads all lines in the text file
            lines = f.readlines()
        with open("src/bookings_list.txt", "w") as f: #Deletes and re writes all lines except for the original booking
            for line in lines:
                if line != booking and line.strip() != "":
                    f.write(line)
            if delete == False:
                f.write("\n" + new_booking) #Adds the new(edited) booking
                print("Your booking has successfully been edited")
                sleep(3)
            elif delete == True: #Will not add the booking, just leaving original deleted
                print("The booking has successfully been deleted")
                sleep(3)
