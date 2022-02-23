s = str(input("Enter IP address:"))
if "." in s and "[.]" not in s:
    s = s.replace(".", "[.]")
else: print("Invalid IP!!!", end = " ")
print(s)
