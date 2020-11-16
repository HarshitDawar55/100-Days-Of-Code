import random
import HangmanLogo

# Adding HangMan Stages
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(HangmanLogo.logo)
# Adding words to the game
words = ['abruptly',
         'absurd',
         'abyss',
         'affix',
         'askew',
         'avenue',
         'awkward',
         'axiom',
         'azure',
         'bagpipes',
         'bandwagon',
         'banjo',
         'bayou',
         'beekeeper',
         'bikini',
         'blitz',
         'blizzard',
         'boggle',
         'bookworm',
         'boxcar',
         'boxful',
         'buckaroo',
         'buffalo',
         'buffoon',
         'buxom',
         'buzzard',
         'buzzing',
         'buzzwords',
         'caliph',
         'cobweb',
         'cockiness',
         'croquet',
         'crypt',
         'curacao',
         'cycle',
         'daiquiri',
         'dirndl',
         'disavow',
         'dizzying',
         'duplex',
         'dwarves',
         'embezzle',
         'equip',
         'espionage',
         'euouae',
         'exodus',
         'faking',
         'fishhook',
         'fixable',
         'fjord',
         'flapjack',
         'flopping',
         'fluffiness',
         'flyby',
         'foxglove',
         'frazzled',
         'frizzled',
         'fuchsia',
         'funny',
         'gabby',
         'galaxy',
         'galvanize',
         'gazebo',
         'giaour',
         'gizmo',
         'glowworm',
         'glyph',
         'gnarly',
         'gnostic',
         'gossip',
         'grogginess',
         'haiku',
         'haphazard',
         'hyphen',
         'iatrogenic',
         'icebox',
         'injury',
         'ivory',
         'ivy',
         'jackpot',
         'jaundice',
         'jawbreaker',
         'jaywalk',
         'jazziest',
         'jazzy',
         'jelly',
         'jigsaw',
         'jinx',
         'jiujitsu',
         'jockey',
         'jogging',
         'joking',
         'jovial',
         'joyful',
         'juicy',
         'jukebox',
         'jumbo',
         'kayak',
         'kazoo',
         'keyhole',
         'khaki',
         'kilobyte',
         'kiosk',
         'kitsch',
         'kiwifruit',
         'klutz',
         'knapsack',
         'larynx',
         'lengths',
         'lucky',
         'luxury',
         'lymph',
         'marquis',
         'matrix',
         'megahertz',
         'microwave',
         'mnemonic',
         'mystify',
         'naphtha',
         'nightclub',
         'nowadays',
         'numbskull',
         'nymph',
         'onyx',
         'ovary',
         'oxidize',
         'oxygen',
         'pajama',
         'peekaboo',
         'phlegm',
         'pixel',
         'pizazz',
         'pneumonia',
         'polka',
         'pshaw',
         'psyche',
         'puppy',
         'puzzling',
         'quartz',
         'queue',
         'quips',
         'quixotic',
         'quiz',
         'quizzes',
         'quorum',
         'razzmatazz',
         'rhubarb',
         'rhythm',
         'rickshaw',
         'schnapps',
         'scratch',
         'shiv',
         'snazzy',
         'sphinx',
         'spritz',
         'squawk',
         'staff',
         'strength',
         'strengths',
         'stretch',
         'stronghold',
         'stymied',
         'subway',
         'swivel',
         'syndrome',
         'thriftless',
         'thumbscrew',
         'topaz',
         'transcript',
         'transgress',
         'transplant',
         'triphthong',
         'twelfth',
         'twelfths',
         'unknown',
         'unworthy',
         'unzip',
         'uptown',
         'vaporize',
         'vixen',
         'vodka',
         'voodoo',
         'vortex',
         'voyeurism',
         'walkway',
         'waltz',
         'wave',
         'wavy',
         'waxy',
         'wellspring',
         'wheezy',
         'whiskey',
         'whizzing',
         'whomever',
         'wimpy',
         'witchcraft',
         'wizard',
         'woozy',
         'wristwatch',
         'wyvern',
         'xylophone',
         'yachtsman',
         'yippee',
         'yoked',
         'youthful',
         'yummy',
         'zephyr',
         'zigzag',
         'zigzagging',
         'zilch',
         'zipper',
         'zodiac',
         'zombie', "business", "kale", "vegetables", "pomegranate", "bear", "harshitdawar", "queen", "king"]

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
        # Checking that whether the previous guessed word in again guessed or not!
        if guess in toDisplay:
            print("You have already guessed {}\n".format(guess))
        # If the guessed word is wrong
        elif guess not in selectedWord:
            chancesLeft -= 1
            print("You guessed {}, it's not present in the word!".format(guess))
            print(stages[chancesLeft])
            if chancesLeft == 0:
                print("You Lose")
                print("Word was: {}".format(selectedWord))
            else:
                print(f"You left with lives {chancesLeft}")
        else:
            for position in range(len(selectedWord)):
                if guess == selectedWord[position]:
                    toDisplay[position] = guess
            print("""Word is '{}'""".format(' '.join(toDisplay)))
