from bookings import add_booking
from bookings import edit_booking


def test_add_booking(monkeypatch): #This test adds a booking and checks bookings.txt to ensure it is there
    inputs = iter(["testy", "test", "1", "0930", "3", "y"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    add_booking()
    bookings_file = open("src/bookings_list.txt", "r")
    target = "0930 1 testy test 3"
    result = ""
    for line in bookings_file.readlines():
        if line.strip() == target:
            result = line
    assert target in result

def test_edit_booking(monkeypatch):
    original = "0930 1 testy test 3"
    inputs = iter(["1", "editing", "test", "2", "2", "1230", "3", "8", "5", "y", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    edit_booking(original)
    bookings_file = open("src/bookings_list.txt", "r")
    target = "1230 2 editing test 8"
    result = ""
    for line in bookings_file.readlines():
        if line.strip("\n") == target:
            result = line
    assert target == result
    delete_test(target)

def delete_test(target):
    with open("src/bookings_list.txt", "r") as f: #This will delete the test booking after checking it is there
        lines = f.readlines()
    with open("src/bookings_list.txt", "w") as f:
        for line in lines:
            if line != target and line.strip() != "":
                f.write(line)
