from sys_display import system_display 

def test_grey_bar():
    assert system_display(-1) == "invalid" # test dengan invalid input
    assert system_display(5) == "grey bar" # test dengan valid input


def test_green_bar():
    assert system_display(20) == "green bar" # test dengan valid input


def test_yellow_bar():
    assert system_display(56) == "yellow bar" # test dengan valid input


def test_red_bar():
    assert system_display(90) == "red bar" # test dengan valid input
    assert system_display(230) == "invalid" # test dengan invalid input