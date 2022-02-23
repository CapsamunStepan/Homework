s = str(input("Enter string:"))
i = 0
num = len(s)
while i < num:
    s += s[num - 1 - i]
    i += 1
s = s[num:]
print(s)
