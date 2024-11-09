num = int(input("Adj meg egy egész pozitív számot: ").strip())

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
print("***************")
for i in range(10, 100):
    x = str(i)
    a = int(x[0])
    b = int(x[1])

    if a + b == 10:
        print(i)