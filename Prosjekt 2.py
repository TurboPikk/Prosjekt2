#Login
poop = {
        "Hadi" : "admin123"
    }

def login_info(stored, attempt):
    if attempt == stored:
        return True
    else:
        print("Your login was not successful. Please try again: ")
        return False


def login():
    user = input("Enter your username: ")
    passw = input("Enter your password: ")
    check = {
        user : passw
    }
    return(check)

while True:
    x = login_info(poop, login())

    if x == True:
        print("poop")
        break
    else:
        print("fart")
    