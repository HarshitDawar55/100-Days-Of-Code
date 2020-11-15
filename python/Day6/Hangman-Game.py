import random

# Adding words to the game
words = ["business", "kale", "vegetables", "pomegranate", "bear", "harshitdawar", "queen", "king"]

selectedWord = random.choice(words)

# Displaying an empty word!
toDisplay = []
for i in range(len(selectedWord)):
    toDisplay.append("_")

print(" ".join(toDisplay))

chancesLeft = 6
while chancesLeft > 0:
    if "_" not in toDisplay:
        print("You Won!")
        break
    else:
        guess = input("Guess a word!\n")
        if guess not in selectedWord:
            chancesLeft -= 1
            if chancesLeft == 0:
                print("You Lose")
            else:
                print(f"You left with lives {chancesLeft}")
        else:
            for position in range(len(selectedWord)):
                if guess == selectedWord[position]:
                    toDisplay[position] = guess
            print("""Word is '{}'""".format(' '.join(toDisplay)))
