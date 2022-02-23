from array import *

n = int(input("Enter the number of numbers:"))
a = array("i", range(n))

for i in range(n):
    a[i] = int(input(f'a[{i}] = '))

for i in range(n):
    for j in range(n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
            
for i in range(n):
    print(a[i], end = " ")
