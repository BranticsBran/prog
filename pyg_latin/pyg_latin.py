def welcome():
    welcome_msg = """
    =======================================
    Sup, Scrub.
    Welcome to Pig Latin 101 taught by yours trully, Comrade Doge.
    =======================================
    """
    print(chr(27) + "[2J")
    print welcome_msg

def to_pyg():
    original = get_user_input()
    if is_valid(original) and to_quit(original):
        pyg = 'ay'
        word = original.lower()
        first = word[0]
        new_word = word + first + pyg
        new_word = new_word[0:len(new_word)]
        print """

        That's a cool word, Scrub, here it is in Pig Latin: """ + new_word[1:len(new_word)]+ """

        """
        to_pyg()
    elif to_quit(original) == False:
        print """                 ============================
                    Peace out, Scrublord.
                 ============================"""
        return
    else:
        error()

def error():
        print """
        =================================================================================================
        Hey! You didn't type anything, or you have a character at isn't a letter in your word! Try again!
                                       (spaces included)
        =================================================================================================
              """
        to_pyg()

def is_valid(x):
    if len(x) > 0 and x.isalpha():
        return True
    else:
        return False
def to_quit(x):
    if x == 'Z':
        return False
    else:
        return True

def get_user_input():
    return raw_input('Enter a word or "Z" to Quit:')

def loop():
    welcome()
    to_pyg()

loop()
