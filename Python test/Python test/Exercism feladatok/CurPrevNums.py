for i in range (10):
    x = str(i)
    a = int(x[0])
    b = a - 1
    if a == 0:
        b = 0
    print(f"The current number: {a}, The previous number: {b}, Sum: {a+b}")