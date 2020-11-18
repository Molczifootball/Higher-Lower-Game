import random
from art import *
from game_data import *
import replit

to_compare = []
if_lost = 0
score = 0 

def choose_accounts():
  accounts = []
  acc1 = data[random.randint(0,len(data)-1)]
  acc2 = data[random.randint(0,len(data)-1)]
  while acc1 == acc2:
    acc2 = data[random.randint(0,len(data)-1)]
  accounts.append(acc1)
  accounts.append(acc2)
  return accounts

def check_winner(per1,per2):
  if per1["follower_count"] > per2["follower_count"]:
    return per1
  elif per1["follower_count"] < per2["follower_count"]:
    return per2

def gameover():
  print("Game over")
  print(f"Your score is {score}")
  again = input("Wanna play again ? Press Y and Enter")
  if again == "Y" or again =="y":
    if_lost = 0
    play(if_lost)

def play(if_lost):
  global score 
  print(logo)
  while not if_lost==1:
    replit.clear()
    print(logo)
    to_compare = choose_accounts()
    person1 = to_compare[0]
    person2 = to_compare[1]
    print("Who do you think got more followers ?")
    print(f"YOUR CURRENT SCORE IS: {score}")
    print(f'{person1["name"]}, the {person1["description"]} from {person1["country"]}')
    print("OR")
    print(f'{person2["name"]}, the {person2["description"]} from {person2["country"]}')
    answer = input("A or B ? ")
    if answer == "A" or answer == "a":
      answer = person1
    elif answer == "B" or answer == "b":
      answer = person2
    winner = check_winner(person1,person2)
    if answer == winner:
      score += 1
      ("You WON ! Proceed to next round.")
    else:
      if_lost = 1
      gameover()

play(if_lost)
