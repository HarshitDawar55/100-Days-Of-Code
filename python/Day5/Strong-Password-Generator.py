import random

# Defining a Symbol List!
symbolList = ["&", "%", "$", "(", ")", "#", "@"]

# Taking Input from the user!
letters = int(input("Enter the number of letters in the password!\n"))
numbers = int(input("Enter the number of digits in the password!\n"))
symbols = int(input("Enter the number of symbols in the password!\n"))

password = []

for i in range(letters):
    temp = random.randint(1, 100)
    if temp % 2 == 0:
        password.append(chr(random.randint(65, 90)))
    else:
        password.append(chr(random.randint(97, 122)))

for i in range(numbers):
    password.append(chr(random.randint(48, 57)))

for i in range(symbols):
    password.append(random.choice(symbolList))

# Shuffling the generated characters to create a powerful unbeatable password
random.shuffle(password)
print("Strong Password Generated is: {}".format("".join(password)))
