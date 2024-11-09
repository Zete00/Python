normal = input("Type in the ISBN-10 number: ").strip()
isbn = normal.upper().replace("-", "")

d1 = int(isbn[0])
d2 = int(isbn[1])
d3 = int(isbn[2])
d4 = int(isbn[3])
d5 = int(isbn[4])
d6 = int(isbn[5])
d7 = int(isbn[6])
d8 = int(isbn[7])
d9 = int(isbn[8])

if isbn[9] == "X":
    dX = 10
else:
    dX = int(isbn[9])

test = (d1 * 10 + d2 * 9 + d3 * 8 + d4 * 7 + d5 * 6 + d6 * 5 + d7 * 4 + d8 * 3 + d9 * 2 + dX) % 11

if (test == 0):
    print(f"{normal} is a valid ISBN-10 number.")
else:
    print(f"{normal} is not a valid ISBN-10 number.")