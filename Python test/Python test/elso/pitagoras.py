import math

x = float(input("Add meg az egyik befogót: "))
y = float(input("Add meg a másik befogót: "))

print("A pitagorasz tétel: a^2 + b^2 = c^2")
print(f"{x}^2 + {y}^2 = c^2")
print(f"{x**2} + {y**2} = c^2")
print(f"{x**2 + y**2} = c^2")
print(f"{math.sqrt(x**2 + y**2)} = c")