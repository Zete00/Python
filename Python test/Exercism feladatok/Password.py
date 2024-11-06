import random

Chars = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "," "%", "!", "-", "_"] 
Choice = input("Akarsz számítógép által generált jelszót? (Y/N): ").strip().upper()
while Choice not in "YN":
    print("Egy érvényes értéket adj meg.")
    Choice = input("Akarsz számítógép által generált jelszót? (Y/N): ").strip().upper()
if Choice == "Y":
    approve = None
    while approve != "Y":
        Gen = random.choices(Chars, k=10)
        c0 = Gen[0]
        c1 = Gen[1]
        c2 = Gen[2]
        c3 = Gen[3]
        c4 = Gen[4]
        c5 = Gen[5]
        c6 = Gen[6]
        c7 = Gen[7]
        c8 = Gen[8]
        c9 = Gen[9]
        UserPass = str(c0 + c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9)
    approve = input(f"Do you like this password: {UserPass} ? (Y/N): ").strip().upper()
else:
    UserPass = input("Adj meg egy új jelszót: ")
    while len(UserPass) != 10:
        print("A jelszónak 10 karakteresnek kell lennie.")
        UserPass = input("Adj meg egy új jelszót: ")
    while UserPass[0] or UserPass[1] or UserPass[2] or UserPass[3] or UserPass[4] or UserPass[5] or UserPass[6] or UserPass[7] or UserPass[8] or UserPass[9] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print("A jelszónak tartalmazia kell legalább 1 NAGYBETŰS karaktert.")
        UserPass = input("Adj meg egy új jelszót: ")
    while UserPass[0] or UserPass[1] or UserPass[2] or UserPass[3] or UserPass[4] or UserPass[5] or UserPass[6] or UserPass[7] or UserPass[8] or UserPass[9] not in "abcdefghijklmnopqrstuvwxyz":
        print("A jelszónak tartalmazia kell legalább 1 kisbetűs karaktert.")
        UserPass = input("Adj meg egy új jelszót: ")
    while UserPass[0] or UserPass[1] or UserPass[2] or UserPass[3] or UserPass[4] or UserPass[5] or UserPass[6] or UserPass[7] or UserPass[8] or UserPass[9] not in "0123456789":
        print("A jelszónak tartalmazia kell legalább 1 számot.")
        UserPass = input("Adj meg egy új jelszót: ")
    while UserPass[0] or UserPass[1] or UserPass[2] or UserPass[3] or UserPass[4] or UserPass[5] or UserPass[6] or UserPass[7] or UserPass[8] or UserPass[9] not in ".,%!-_":
        print("A jelszónak tartalmazia kell legalább 1 speciális karaktert.")
        UserPass = input("Adj meg egy új jelszót: ")
    approve = (f"Az új jelszód {UserPass} lesz. Biztos vagy ebbe? (Y/N): ").strip().upper()

if approve == "Y":
    print(f"Your new password is {UserPass}")