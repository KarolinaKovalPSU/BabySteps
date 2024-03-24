import random

def fortune_teller():

  destiny = ["You'll be rich",
             "Bad day",
             "Say sorry",
             "Someone loves you",
             "Solutions are within reach",
             "Wait. It's not yet time"]

  oracle = random.choice(destiny)
  question = input("Press enter to know your destiny\n")

  if question == "":
      print(oracle)
      next_try = input("Type Yes to try again\n")
      if next_try == "Yes":
          fortune_teller()
      else: print("okay!")
  else:
      print("Oops, wrong input")
fortune_teller()