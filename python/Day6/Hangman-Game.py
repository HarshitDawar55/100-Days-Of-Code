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
            print(f"You left with lives {chancesLeft}")
        else:
            index = selectedWord.index(guess)
            toDisplay[index] = guess
            print(f"Word is {' '.join(toDisplay)}")
