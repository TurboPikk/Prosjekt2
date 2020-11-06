#Login
poop = { "MEK1300" : "Python" }

def login():
    while True:
        check = { input("Enter your username: ") : input("Enter your password: ") }
        if login_info(poop, check) == True:
            print("fart")
            break
        else:
            print("Invalid  username  and/or  password")

def login_info(stored, attempt):
    if stored == attempt:
        return True
    else:
        return False


login()
    