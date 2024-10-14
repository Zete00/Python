def is_armstrong_number(number):
    s = str(number)
    l = len(s)
    total = sum([int(i)**l for i in s])
    if number == total:
        print(number)