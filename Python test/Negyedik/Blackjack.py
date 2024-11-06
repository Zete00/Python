import random

Chips = 1000

Types = ["Clubs", "Diamonds", "Hearts", "Spades"]
Num = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

DFinal1 = [None]
DFinal2 = [None]
PFinal1 = [None]
PFinal2 = [None]

while DFinal1 == DFinal2 or DFinal1 == PFinal1 or DFinal1 == PFinal2 or DFinal2 == PFinal1 or DFinal2 == PFinal2 or PFinal1 == PFinal2:

    if None in DFinal1:
        DFinal1.remove(None)
    if None in DFinal2:
        DFinal2.remove(None)
    if None in PFinal1:
        PFinal1.remove(None)
    if None in PFinal2:
        PFinal2.remove(None)

    DNum1 = random.choice(Num)
    DNum2 = random.choice(Num)
    PNum1 = random.choice(Num)
    PNum2 = random.choice(Num)

    Dtype1 = random.choice(Types)
    Dtype2 = random.choice(Types)
    Ptype1 = random.choice(Types)
    Ptype2 = random.choice(Types)

    DFinal1.append(Dtype1)
    DFinal2.append(Dtype2)
    PFinal1.append(Ptype1)
    PFinal2.append(Ptype2)

    DVal1 = None
    DVal2 = None
    PVal1 = None
    PVal2 = None

    Dt1 = None
    Dt2 = None
    Pt1 = None
    Pt2 = None

    if DNum1 == "Jack" or DNum1 == "Queen" or DNum1 == "King":
        DVal1 = 10
    elif DNum1 == "Ace":
        DVal1 = 11
    else:
        DVal1 = int(DNum1)

    DFinal1.append(DVal1)    
    
    if DNum2 == "Jack" or DNum2 == "Queen" or DNum2 == "King":
        DVal2 = 10
    elif DNum2 == "Ace":
        DVal2 = 11

        if DVal1 + DVal2 >= 22:
            DVal2 = 1
    else:
        DVal2 = int(DNum2)

    DFinal2.append(DVal2)

    if PNum1 == "Jack" or PNum1 == "Queen" or PNum1 == "King":
        PVal1 = 10
    elif PNum1 == "Ace":
        PVal1 = 11
    else:
        PVal1 = int(PNum1)

    PFinal1.append(PVal1)
    
    if PNum2 == "Jack" or PNum2 == "Queen" or PNum2 == "King":
        PVal2 = 10
    elif PNum2 == "Ace":
        PVal2 = 11

        if PVal1 + PVal2 >= 22:
            PVal2 = 1
    else:
        PVal2 = int(PNum2)

    PFinal2.append(PVal2)

print()
print(f"Your hand is: {PNum1} of {Ptype1} and {PNum2} of {Ptype2}.")
print(f"The value of your cards is: {PVal1 + PVal2}")
print()
print(f"The Dealers hand is: {DNum1} of {Dtype1} and -- of --.")
print()

