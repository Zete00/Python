liter = float(input("Add meg a festék literjének árát (HUF): ").strip())
szobaA = float(input("Add meg a szoba hosszúságát (m): ").strip())
szobaB = float(input("Add meg a szoba szélességét (m): ").strip())
szobaC = float(input("Add meg a szoba magasságát (m): ").strip())
festoora = float(input("Add meg a festő órabérét (HUF): ").strip())
festotime = float(input("Add meg a festő gyorsaságát (m^2/h): ").strip())
festekreteg = int(input("Add meg hány rétegben akarod festeni a szobát: ").strip())

szoba = szobaA * szobaB + 2 * szobaB * szobaC + 2 * szobaC * szobaA
festekar = szoba / 5.7 * festekreteg * liter
festoar = szoba / festotime * festoora
osszar = festekar + festoar 

print(f"A szoba kifestése {osszar} HUF-ba fog kerülni. A festő {festoar} HUF-ba, a festék {festekar} HUF-ba kerül.")