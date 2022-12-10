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
    if edit_continue == 1:
        edit_booking(selected_booking)




def edit_booking(booking):
    bookings_file = open("src/bookings_list.txt", "a+")
    user_input = input("What would you like to change? ")
    print("1 - Name")
    print("2 - Time")
    print("3 - PAX")

search_booking()
