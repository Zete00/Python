import random

Choice = input("Full Random (FR) vagy Kevésbé Random (KR)? ").strip().upper()
UserInput = int(input("Adj meg egy egész számot 1 és 1000 között: ").strip())
while UserInput < 1 or UserInput > 1000:
    UserInput = int(input("Adj meg egy egész számot 1 és 1000 között: ").strip())
tries = 0
CompNum = None
low = 1
high = 1000

if Choice == "FR":
    while UserInput != CompNum:
        tries = tries + 1
        CompNum = random.randint(1,1000)
    print(f"A számítógép eltalálta a(z) {UserInput} számot {tries} próbálkozásból.")

elif Choice == "KR":
    while UserInput != CompNum:
        tries = tries + 1
        CompNum = random.randint(low, high)
        if UserInput < CompNum:
            high = CompNum - 1
        elif UserInput > CompNum:
            low = CompNum + 1
    print(f"A számítógép eltalálta a(z) {UserInput} számot {tries} próbálkozásból.")