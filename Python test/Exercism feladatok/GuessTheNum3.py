import random

print("Gondolj egy egész számra 1 és 100 között.")

low = 1
high = 100
UserInput = None
tries = 0 

while UserInput != "H":
    tries = tries + 1
    if low + 1 == high - 1:
            UserInput = "H"
    guess = random.randint(low, high)
    UserInput = input(f"A számítógép {guess}-re gondolt. Ez a szám kisseb (K), nagyobb (N) vagy helyes (H): ").strip().upper()
    while UserInput not in "KNH":
         print("Adj meg egy helyes értéket.")
         UserInput = input(f"A számítógép {guess}-re gondolt. Ez a szám kisseb (K), nagyobb (N) vagy helyes (H): ").strip().upper()
    if UserInput == "N":
        low = guess + 1
    elif UserInput == "K":
        high = guess - 1
print(f"A számítógép kitalálta a(z) {guess} számot {tries} próbából.")