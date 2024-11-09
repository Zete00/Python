import random

RPS = ["Rock", "Paper", "Scissors"]
valasz = input("Choose Rock, Paper, or Scissors: ").capitalize().strip()
x = random.choice(RPS)

if valasz not in RPS:
    print("Please choose a valid option: Rock, Paper, or Scissors.")
else:
    print(f"Computer chose: {x}")
    
    if valasz == x:
        print("Tie!")
    elif (valasz == "Rock" and x == "Scissors") or (valasz == "Paper" and x == "Rock") or (valasz == "Scissors" and x == "Paper"):
        print("You win!")
    else:
        print("You lost!")
