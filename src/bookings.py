# Create home page where user selects options to choose from
bookings_file = open("src/bookings_list.txt", "a+")
def home_page():
    print("1 - View today's bookings")
    print("2 - Add a booking")
    print("3 - Edit a booking")
    user_input = input("Please select an option: ")
    if user_input == 2:
        add_booking()

def add_booking():
    name = input("Please enter name: ")
    while True:
        print("1 - Breakfast")
        print("2 - Lunch")
        print("3 - Dinner")
        service = int(input("Please enter a number to select service: "))
        if service <= 0 or service > 3:
            print("Please select a valid option")
            continue
        else:
            break
    if service == 1:
        while True:
            time = int(input("Please enter a time between 0700 and 1200: "))
            if time < 700 or time > 1200:
                print("Please enter a valid time")
                continue
            else:
                break
    pax = input("How many guests are attending?: ")
    new_booking = str(name + " " + str(service) + " " + str(time) + " " + str(pax))
    bookings_file.write("\n" + new_booking)
        

add_booking()
# Function to add new booking