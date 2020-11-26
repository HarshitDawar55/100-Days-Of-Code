import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


# Function to Deal a Card!
def deal_a_card():
    cardValues = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cardValues)


# Function to calculate points from the cards!
def calculate_points(handOfCards):
    if len(handOfCards) == 2 and sum(handOfCards) == 21:
        return 1
    elif sum(handOfCards) > 21 and 11 in handOfCards:
        i = handOfCards.index(11)
        handOfCards.remove(11)
        handOfCards.insert(i, 1)
        return sum(handOfCards)
    else:
        return sum(handOfCards)


# Function to check the Final Result!
def FinalResult(userScore, computerScore):
    if userScore == computerScore:
        print("It's a Draw!")
    elif computerScore == 1:
        print("You Lose, opponent has a BlackJack!")
    elif userScore == 1:
        print("You Win, you have a BlackJack!")
    elif computerScore > 21:
        print("You Win, opponent exceeds 21!")
    elif userScore > 21:
        print("You Lose, you exceeds 21!")
    elif userScore > computerScore:
        print("You Win!")
    else:
        print("You Lose!")


# Function to Execute the Complete Game!
def executeGame():
    print(logo)
    userCards, computerCards = [], []

    for _ in range(2):
        userCards.append(deal_a_card())
        computerCards.append(deal_a_card())

    while True:
        userScore = calculate_points(userCards)
        computerScore = calculate_points(computerCards)
        print(f"You Cards are: {userCards},\n Your Points are: {userScore}")
        print(f"Opponent First Card is: {computerCards[0]},\n Your Points are: {calculate_points(userCards)}")

        if userScore == 1 or computerScore == 1 or userScore > 21:
            break
        else:
            choice = input("You Want another Card: 'yes' or 'no': ")
            if choice.lower() == "yes":
                userCards.append(deal_a_card())
            elif choice.lower() == "no":
                break
            else:
                print("Wrong Choice! ")

    # Making Computer Deal cards for itself
    while computerScore != 1 or computerScore < 17:
        computerCards.append(deal_a_card())
        computerScore = calculate_points(computerCards)

    # Printing the Final Results!
    print(f"You Final set of Cards: {userCards}, You Total Points: {userScore}")
    print(f"Opponent's Final set of Cards: {computerCards}, Opponent's Total Points: {computerScore}")
    print(FinalResult(userScore, computerScore))

