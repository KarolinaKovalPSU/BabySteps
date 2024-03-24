
import random

def dice():

  roll = [1, 2, 3, 4, 5, 6]

  number = random.choice(roll)
  question = input("Press enter to roll the dice!\n")

  if question == "":
      print(number)
  else:
      print("Have a nice day!")

while True:
  dice()



