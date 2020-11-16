
from random import randint

def main():
    retard_level = 0
    while play_game(retard_level) == True:
        retard_level += 1
    print("Bye!")



def generate_target(lowest, highest):
    target = randint(lowest, highest)
    return target

def generate_guess(tries):
    guess_loop = True

    while guess_loop == True:
        
        if tries == 1:
            guess = input("Input your first guess: ")
        elif tries == 5:
            guess = input("Input your last guess: ")
        else:
            guess = input("Input your next guess: ")
        print()

        if guess.isnumeric() == True:
            guess = int(guess)

            if 1 <= guess <= 1000:
                guess_loop = False
            else:
                print("Your number must be between 1 and 1000!")
        
        else:
            print("Your input must be an integer!")


    return int(guess)



def check_input(guess, target, tries, retard_level):
    if guess != target:
        if retard_level == 3 and tries > 1:
            print("""
You fucking retard!!!!!!
            """)

        else:
            if guess > target:
                print("Sorry your guess was too high")
            else:
                print("Sorry your guess was too low")
    
        
        print(f"Guesses remaining is {5 - tries}")
        
        
        if retard_level != 0:
            retard_function(guess, target, retard_level)
        
        print("")
                
        return False
    
    else:
        return True


def again():
    again = ""
    while "y" != again != "n":
        again = input("Do you want to play again? (y/n): ")
        if again == "y":
            return True
        elif again == "n":
            return False
    

def play_game(retard_level):
    print("")

    target = generate_target(1, 1000)
    tries = 1

    if retard_level == 3:
        print("\n\n\nCome on! Now you can do it!\n")

    print("Guess a number between 1 and 1000...")
    
    while tries < 6:
        guess = generate_guess(tries)

        if check_input(guess, target, tries, retard_level) == True:
            print(f"Congratulations! You guessed {target} in {tries} tries!")
            tries = 6
            return False        
        tries += 1
    
    if tries == 6:
        print(f"Sorry! The correct number was {target}")
    
    return again()




def retard_function(guess, target, level):

    difference = abs(guess - target)
    exponent = 3 - level
    if exponent == 0:
        exponent = 1

    size = difference // (10 ** exponent)
    magnitude = size*(10**exponent)

    if size == 0:
        print(f"You are less than {10**exponent} away from correct answer...")
    else:
        print(f"You are more than {magnitude} away from correct answer...")




main()