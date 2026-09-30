import random
import time

art = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """,
]

moves = ["rock", "paper", "scissors"]
results = ["Win", "Tie", "Lose"]

def init():
    plr_wins = 0
    comp_wins = 0

    print("Let's play rock paper scissors!")
    turns = int(ask_num("First to "))
    
    while True:
        plr = ask("Rock, Paper, Scissors, Say... Shoot: (r)Rock (p)Paper (s)Scissors ", ["r", "p", "s"])
        choice = turn_handler(plr)

        if choice == "Win": plr_wins += 1
        elif choice == "Lose": comp_wins += 1

        print(f"Player: {plr_wins} Computer: {comp_wins}")
        
        if plr_wins >= turns:
            print("You win! You beat AI!")
            break
        elif comp_wins >= turns:
            print("Computer Wins! You kinda suck...")
            break

def turn_handler(plr):
    num = random.randint(0, 2)
    comp = moves[num]
   
    print(f"Computer: {comp}")
    print(art[num])

    if plr == "r" and comp == "scissors":
        return "Win"
    if plr == "p" and comp == "rock":
        return "Win"
    if plr == "s" and comp == "paper":
        return "Win"
    if plr == comp[0]:
        return "Tie"
    return "Lose"

def ask(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        print(f"Pick one of {', '.join(options)}")

def ask_num(prompt):
    while True:
        choice = int(input(prompt))
        if type(choice) == int:
            return choice
        print("Pick an integer")

init()
