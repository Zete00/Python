mondat = input("Mondj valamit Bobnak: ")

if mondat == "":
    print("Fine. Be that way!")

elif mondat.upper() == mondat and mondat[-1] == "?":
    print("Calm down, I know what I'm doing!")

elif mondat[-1] == "?":
    print("Sure.")

elif mondat.upper() == mondat:
    print("Whoa, chill out!")

else: 
    print("Whatever.")