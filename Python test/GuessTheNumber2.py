import random

x = random.randint(1,100)
UserInput = int(input("Találd ki a véletlenszerű számot, 7 életed van: "))
lives = 7

while UserInput != x:
    if UserInput < x:
        print(f"A szám nagyobb a véletlenszerű számnál.")
        UserInput = int(input("Találd ki a véletlenszerű számot: "))
        lives = lives - 1
        print(f"{lives} életed maradt.")
    elif UserInput > x:
        print(f"A szám kisebb a véletlenszerű számnál.")
        UserInput = int(input("Találd ki a véletlenszerű számot: "))
        lives = lives - 1
        print(f"{lives} életed maradt.")
    if lives == 0:
        print(f"Sajnos vesztettél, a szám {x} volt.")

print(f"Kitaláltad! A szám {x} volt.")