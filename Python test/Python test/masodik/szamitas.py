x = int(input("Adj meg egy pozitív egész számot: "))

valasz = input("Osztható-e? (Ezek közül válassz: 2, 3, 4, 5, 6, 7, 8, 9): ")

if (valasz == "2"):
    if (x % 2 == 0):
        print(f"Osztható! Az eredmény: {x/2}")
    else:
        print(f"Nem osztható! Az eredmény {x/2}")
elif (valasz == "3"):
    if (x % 3 == 0):
        print(f"Osztható! Az eredmény {x/3}")
    else:
        print(f"Nem osztható! Az eredmény {x/3}")
elif (valasz == "4"):
    if (x % 4 == 0):
        print(f"Osztható! Az eredmény {x/4}")
    else:
        print(f"Nem osztható! Az eredmény {x/4}")
elif (valasz == "5"):
    if (x % 5 == 0):
        print(f"Osztható! Az eredmény {x/5}")
    else:
        print(f"Nem osztható! Az eredmény {x/5}")
elif (valasz == "6"):
    if (x % 6 == 0):
        print(f"Osztható! Az eredmény {x/6}")
    else:
        print(f"Nem osztható! Az eredmény {x/6}")
elif (valasz == "7"):
    if (x % 7 == 0):
        print(f"Osztható! Az eredmény {x/7}")
    else:
        print(f"Nem osztható! Az eredmény {x/7}")
elif (valasz == "8"):
    if (x % 8 == 0):
        print(f"Osztható! Az eredmény {x/8}")
    else:
        print(f"Nem osztható! Az eredmény {x/8}")
elif (valasz == "9"):
    if (x % 9 == 0):
        print(f"Osztható! Az eredmény {x/9}")
    else:
        print(f"Nem osztható! Az eredmény {x/9}")
else:
    print("A megadott számok közül válassz!")