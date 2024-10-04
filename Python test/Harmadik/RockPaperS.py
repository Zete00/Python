import random

RPS = ["Rock", "Paper", "Scissors"]
valasz = input("Choose Rock, Paper or Scissors: ").capitalize().strip()
x = random.choice(RPS)

if (valasz not in RPS):
    print("Give a chooseable answer.")
elif (valasz == "Rock" and x == "Rock"):
    print("Tie!")
elif (valasz == "Rock" and x == "Paper"):
    print("You lost!")
elif (valasz == "Rock" and x == "Scissors"):
    print("You win!")
elif (valasz == "Paper" and x == "Rock"):
    print("You win!")
elif (valasz == "Paper" and x == "Paper"):
    print("Tie")
elif (valasz == "Paper" and x == "Scissors"):
    print("You lost!")
elif (valasz == "Scissors" and x == "Rock"):
    print("You lost!")
elif (valasz == "Scissors" and x == "Paper"):
    print("You win!")
else:
    print("Tie!")