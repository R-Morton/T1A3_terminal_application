def search_booking():
    bookings_file = open("src/bookings_list.txt", "r")
    name_search = input("Please type the first or last name of the customer: ")
    matching_names = []
    for line in bookings_file.readlines():
        if name_search == line.split()[2] or name_search == line.split()[3]:
            matching_names.append(line)
    

search_booking()
