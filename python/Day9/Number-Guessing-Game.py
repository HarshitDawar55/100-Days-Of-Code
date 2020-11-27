import random

logo = """
 _   _                 _                 _____                     _               _____                      
| \ | |               | |               |  __ \                   (_)             |  __ \                     
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ \
| |\  | |_| | | | | | | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|
                                                                            __/ |                             
                                                                           |___/                              
"""


def executeGame():
    print("Welcome to the Number Guessing Game! ")
    level = int(input("Enter playing Level '1' for Hard & '2' for easy!"))
    if level == 1:
        number = random.randint(1, 350)
        chancesleft = 15
        while chancesleft > 0:
            n = int(input("Guess a number: "))
            if number == n:
                print(f"Number is {number}, You Won!")
                break
            elif number > n:
                print("You have guessed a bigger number!")
                chancesleft -=1
            else:
                print("You have guessed a smaller number!")
                chancesleft -= 1
    elif level == 2:
        number = random.randint(1, 150)
        chancesleft = 15
        while chancesleft > 0:
            n = int(input("Guess a number: "))
            if number == n:
                print(f"Number is {number}, You Won!")
                break
            elif number > n:
                print("You have guessed a bigger number!")
                chancesleft -= 1
            else:
                print("You have guessed a smaller number!")
                chancesleft -= 1

    else:
        print("Wrong Choice! ")
