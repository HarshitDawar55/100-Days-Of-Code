import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock Paper Scissors Game!")
print("""
Enter your choice:
1: Rock
2: Paper
3: Scissors
""")
choice = int(input())
gameChoices = [rock, paper, scissors]
computerChoice = random.randint(1, 3)

print("Computer Choose: \n{}".format(gameChoices[computerChoice - 1]))
if choice > 3 or choice < 1:
    print("Wrong Choice!")
elif (choice == 1 and computerChoice == 3) or (choice == 2 and computerChoice == 1) or (choice == 3 and computerChoice == 2):
    print("You Win!")
elif choice == computerChoice:
    print("Its a Tie!")
else:
    print("You Lose!")