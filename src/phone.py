import os
from time import sleep
import random

def bookings_phone():
    os.system('clear')
    print("1 - Enter phone number")
    print("2 - Randomly generate number")
    while True:
        user_input = input("Please select an option: ")
        match user_input:
            case '1':
                os.system('clear')
                not_random = True
                break
            case '2':
                os.system('clear')
                not_random = False
                return random_number()
            case _:
                print("Please select a valid option")
                sleep(1)
                os.system('clear')
    while not_random == True: # This is for manually entering phone number
        phone = input("Please enter a phone number: ")
        phone = phone.zfill(1)
        if len(phone) != 10: # Checks the number is 10 digits long
            print("Please enter a valid number")
            sleep(2)
            os.system('clear')
            continue
        elif phone.startswith("04") or phone.startswith("02"): # Checks that number starts with '02' or '04'
            os.system('clear')
            return phone
        else:
            print("Please enter a valid number")
            sleep(2)
            os.system('clear')
            continue

def random_number():
    count = 1
    number = ['0']
    random_num = ""
    for num in range(1, 8 + 1):
        if count == 1:
            random_num = random.choice(['2', '4'])
            number.append(random_num)
            count += 1
        if number[1] == '2' and count == 2:
            number.append('9')
            count += 1
        else:
            random_num = random.randint(0, 9)
            number.append(str(random_num))
            count +=1
    number = ''.join(number)
    return number