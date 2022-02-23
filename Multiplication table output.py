tabel_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for j in tabel_1:
    if j == 10:
        c  = "   "
    elif j >= 5:
        c = "    "
    else: c = "     "
    print(2, "*", j, "=", 2*j, end = c)
    if j == 4:
        print(3, "*", j, "=", 3*j, end = "    ")
    else: print(3, "*", j, "=", 3*j, end = c)    
    print(4, "*", j, "=", 4*j)
    j +=1

print()

for j in tabel_1:
    if j == 10:
        c  = "   "
    elif j >= 2:
        c = "    "
    else: c = "     "
    print(5, "*", j, "=", 5*j, end = c)
    print(6, "*", j, "=", 6*j, end = c)
    print(7, "*", j, "=", 7*j)
    j +=1

print()

for j in tabel_1:
    if j == 10:
        c  = "   "
    elif j >= 2:
        c = "    "
    else: c = "     "
    print(8, "*", j, "=", 8*j, end = c)
    print(9, "*", j, "=", 9*j, end = c)
    print(10, "*", j, "=", 10*j)
    j +=1
