a = int(input("Enter parameter a:"))
b = int(input("Enter parameter b:"))
c = int(input("Enter parameter c:"))

print("ax", chr(178), " + bx + c = 0", sep = "")
print(a, "x", chr(178), " + ", b, "x + ", c, " = 0", sep = "")
d = b ** 2 - 4 * a * c;
print(d);
if a == 0:
    if b == 0:
        if c == 0:
            print("Infinity number of roots!!!")
        else:
            print("No roots!")
    else:
        x1 = -c / b
        print("x1 =", x1)    
else:
    if d > 0:
        d **= 0.5
        x1 = (-b - d) / (2 * a)
        x2 = (-b + d) / (2 * a)
        print("x1 =", x1, "x2 =", x2)
    elif d == 0:
        x1 = (-b) / (2 * a)
        print("x1 =", x1)
    else: print("No roots!")

