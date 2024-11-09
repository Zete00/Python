# Collect last name
Veznev = input("Add meg a vezetékneved: ")
if Veznev == "":
    print("Adj meg legalább 1 karaktert a vezetéknevedhez!")
    Veznev = input("Add meg a vezetékneved: ")  # Re-prompt if empty

# Collect first name
Kernev = input("Add meg a keresztneved: ")
if Kernev == "":
    print("Adj meg legalább 1 karaktert a keresztnevedhez!")
    Kernev = input("Add meg a keresztneved: ")  # Re-prompt if empty

# Collect age and check if it's valid
Age = int(input("Add meg az életkorod: "))
if Age < 14:
    print("Túl fiatal vagy a weboldal használatához!")

# Ask for nickname
Kellbecnev = input("Akarsz becenevet? (Igen/Nem): ").strip().capitalize()

if Kellbecnev == "Nem":
    print(f"Üdvözöllek {Veznev} {Kernev}! Életkorod: {Age}")
elif Kellbecnev == "Igen":
    becenev = input("Add meg a beceneved: ")
    print(f"Üdvözöllek {becenev} ({Veznev} {Kernev})! Életkorod: {Age}")
else:
    print("Érvénytelen válasz a becenév kérdésre.")


