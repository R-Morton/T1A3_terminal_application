import add_bookings
import search_edit

#python -m pytest -s

def test_add_booking(monkeypatch): #This test adds a booking and checks bookings.txt to ensure it is there
    inputs = iter(["testy", "test", "1", "0438228683", "1", "0930", "3", "y"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    add_bookings.add_booking()
    bookings_file = open("src/bookings_list.txt", "r")
    target = "0930 1 testy test 0438228683 3"
    result = ""
    for line in bookings_file.readlines():
        if line.strip() == target:
            result = line
    assert target in result

def test_edit_booking(monkeypatch): #This test edits the test booking and checks bookings.txt if its there
    original = "0930 1 testy test 0438228683 3"
    inputs = iter(["1", "editing", "test", "2", "1", "0409115100", "3", "2", "1230", "4", "8", "7", "y"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    search_edit.edit_booking(original)
    bookings_file = open("src/bookings_list.txt", "r")
    target = "1230 2 editing test 0409115100 8"
    result = ""
    for line in bookings_file.readlines():
        if line.strip("\n") == target:
            result = line
    assert target == result
    delete_test(target)

def delete_test(target): #This will delete the test booking after checking it is there
    with open("src/bookings_list.txt", "r") as f: 
        lines = f.readlines()
    with open("src/bookings_list.txt", "w") as f:
        for line in lines:
            if line != target and line.strip() != "":
                f.write(line)
