"""The purpose of this program is to roll a quantity number of die type dice and provide the user with the results"""
import random

die = input("What die type (default is d6): ") or "d6" #Promtps user for the type of die to roll or defaults to a six sided die
quantity = input("How many (default is 1): ") or 1 #Prompts user for the number of dice to roll or defaults to 1
quantity = int(quantity) #Changes the user provided information (a string) into an integer for use in the range call in the for loop.
total = 0 #Set total to 0

#There is probably a more eliegant way to do this but I don't know how
if die == "d4":
   sides = 4
elif die == "d6":
   sides = 6
elif die == "d10":
   sides = 10
elif die == "d12":
   sides = 12
elif die == "d20":
   sides = 20
elif die == "d100":
   sides = 100
else:
   print("That is not a die type")

for i in range(0, quantity): #Iterates through the quantity of dice to be rolled and dieplays their individual results
   result = (random.randint(1, sides))
   print(i+1, die, " = ", result)
   total += result
print("This is the result of your roll: ", total)
