"""This program returns the love score of two persons!"""

person1 = input("Enter Your Name!\n")
person2 = input("Enter your Lover Name! \n")

concatenatedString = (person1 + person2).lower()

t_count = concatenatedString.count("t")
r_count = concatenatedString.count("r")
u_count = concatenatedString.count("u")
e_count = concatenatedString.count("e")

true = t_count + r_count + u_count + e_count

l_count = concatenatedString.count("l")
o_count = concatenatedString.count("o")
v_count = concatenatedString.count("v")
e_count = concatenatedString.count("e")

love = l_count + o_count + v_count + e_count

loveScore = int(str(true) + str(love))

if loveScore < 10 or loveScore > 90:
    print(f"Your Love Score is {loveScore}, You are similar to Coke & Mentos Together!")
elif 40 <= loveScore <= 50:
    print(f"Your Love Score is {loveScore}, You are Amazing Together!")
else:
    print(f"Your Love Score is {loveScore}!")
