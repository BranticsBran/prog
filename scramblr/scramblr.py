from crlib import encrypt, decrypt

def welcome():
    welcome_msg = """
    =======================================
    WELCOME TO SCRAMBLR!
    Thanks for stopping by,

    so..

    What would you like to do?

    0: Encrypt data
    1: Decrypt data
    2: Blow this popsickle stand!
    =======================================
    """
    print welcome_msg


def scrambl():
    inp = raw_input('Please enter an encryption key:  ')
    data = raw_input('Enter unencrypted data:  ')
    scrambl = encrypt(inp, data)
    f = open('cache/bc.store','w+')
    f.write(scrambl) # python will convert \n to os.linesep
    f.close()
    scramblr()
def d_scrambl():
    inp = raw_input('Please enter an encryption key:  ')
    file = open('cache/bc.store','r')
    data = file.read()
    file.close()
    raw_text = decrypt(inp, data)

    dfile = open('cache/ad.store','w+')
    dfile.write(raw_text)
    dfile.close()
    scramblr()


def scramblr():

    direction = raw_input('Command: ')
    if direction == '0':
        scrambl()
    elif direction == '1':
        d_scrambl()
    elif direction == '2':
        print 'Peace \m/'

def loop():
    welcome()
    scramblr()

loop()
