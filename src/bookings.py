# Create home page where user selects options to choose from
bookings_file = open("src/bookings_list.txt", "r+")
def home_page():
    print("1 - View today's bookings")
    print("2 - Add a booking")
    print("3 - Edit a booking")
    user_input = input("Please select an option: ")
home_page()


# Function to add new booking
# 