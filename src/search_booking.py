from add_booking import booking_name
from add_booking import booking_time
from add_booking import pax
from add_booking import confirm_booking
def search_booking():
    bookings_file = open("src/bookings_list.txt", "r")
    name_search = input("Please type the first or last name of the customer: ")
    matching_names = []
    results = 0
    for line in bookings_file.readlines():
        if name_search == line.split()[2] or name_search == line.split()[3]:
            results += 1
            matching_names.append(line)
            print(f"{line}")
        else:
            continue
    user_input = int(input("Please select from the matches: "))
    count = 1
    for booking in matching_names:
        if user_input == count:
            selected_booking = booking
            print(selected_booking)
            break
        else:
            count += 1
            continue
    edit_continue = input("Please press 1 to edit or 0 to go back: ")
    if edit_continue == '1':
        edit_booking(selected_booking)




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
    

#edit_booking()
search_booking()
