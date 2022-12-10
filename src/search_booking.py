def search_booking():
    bookings_file = open("src/bookings_list.txt", "r")
    name_search = input("Please type the first or last name of the customer: ")
    selected_booking = ""
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
            print(booking)
            break
        else:
            count += 1
            continue



search_booking()
