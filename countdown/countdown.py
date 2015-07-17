"""This is a program thats will let the user input a time
limit, and begin a countdown."""

def welcome():
    welcome_msg = """
    =======================================
    Sup Yo.

    So this is a countdown timer for all your
    daily needs of counting down things.

    YEAH.

    Enter in your time below.
    =======================================
    """
    print welcome_msg
    countdown()

def countdown(time):
    time = raw_input("Please enter a number to countdown from: ")
    is_valid
    print SUCCESS

    print time

def is_valid(time):
    if len(time) > 0 and x.isalpha():
        return True
    else:
        return False

def main_loop():
    welcome()
    input_time()

main_loop()
