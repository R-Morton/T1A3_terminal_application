bookings_file = open("src/bookings_list.txt", "a+")
def add_booking():
    name = input("Please enter name: ")
    while True:
        print("1 - Breakfast")
        print("2 - Lunch")
        print("3 - Dinner")
        service = int(input("Please enter a number to select service: "))
        if service == 1:
            while True:
                time = int(input("Please enter a time between 0700 and 1200: "))
                if time < 700 or time > 1200:
                    print("Please enter a valid time")
                    continue
                else:
                    break
            break
        if service == 2:
            while True:
                time = int(input("Please enter a time between 1200 and 1530: "))
                if time < 1200 or time > 1530:
                    print("Please enter a valid time")
                    continue
                else:
                    break
            break
        if service == 3:
            while True:
                time = int(input("Please enter a time between 1730 and 2100: "))
                if time < 1730 or time > 2100:
                    print("Please enter a valid time")
                    continue
                else:
                    break
            break
        else:
            print("Please select a valid option")
            continue
    while True:
        pax = int(input("How many guests are attending?: "))
        if pax <= 0:
            print("Please enter atleast one or more guests")
            continue
        elif pax >20:
            print("Bookings above 20 must be refered to the functions team")
            continue
        else:
            break
    new_booking = str(name + " " + str(service) + " " + str(time) + " " + str(pax))
    bookings_file.write("\n" + new_booking)
    bookings_file.flush()
    print("Booking has sucessfully been added")