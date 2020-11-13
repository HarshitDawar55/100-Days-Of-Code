"""This program is used to calculate the Tip for an order!"""

print("\t\t\tWelcome to the Tip Calculator!\t\t\t")
amount = float(input("Enter the total Amount of the Bill!\n"))
tipPercentage = float(input("Enter the Tip Percentage on Total Bill[Do not Enter '%' Symbol]!\n"))
numberOfPeople = int(input("Enter the Number Of People among which the bill is to split!\n"))
amount_for_each_person = (amount * (1 + tipPercentage / 100)) / numberOfPeople

print(f"Each Person has to pay: {round(amount_for_each_person, 2)} INR")