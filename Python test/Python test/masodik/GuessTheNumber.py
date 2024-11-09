import random

Nehezseg = int(input("Add meg a nehézséget (1, 2, 3): ").strip())

if (Nehezseg == 1): 
    x = random.randint(1, 9)
    valasz = int(input("Adj meg egy egész számot 1 és 10 között: ").strip())
    
    if (valasz<1 or 10<valasz):
        print("Adj meg egy számot a megadott számok közül.")
    elif (valasz == x):
        print("Eltaláltad!")
    else: 
        print(f"Sajnos nem talált! A válasz {x}.")

elif (Nehezseg == 2):
    y = random.randint(1, 99)
    valasz = int(input("Adj meg egy egész számot 1 és 100 között: ").strip())

    if (valasz<1 or 100<valasz):
        print("Adj meg egy számot a megatott számok közül.")
    elif (valasz == y):
        print("Eltaláltad!")
    else:
        print(f"Sajnos nem talált! A válasz {y}.")

elif (Nehezseg == 3):
    z = random.randint(1, 999)
    valasz = int(input("Adj meg egy egész számot 1 és 1000 között: ").strip())

    if (valasz<1 or 1000<valasz):
        print("Adj meg egy számot a megadott számok közül.")
    elif (valasz == z):
        print("Eltaláltad!")
    else:
        print(f"Sajnos nem talált! A válasz {z}.")
else:
    print("Érvényes nehézséget adj meg!")