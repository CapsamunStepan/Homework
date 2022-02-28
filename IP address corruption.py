import ipaddress
 
def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    else:
        return True
ip = str(input("Enter IP address:"))
if check_ip(ip):
    ip = ip.replace(".", "[.]")
    print(ip)
else: print("Invalid IP!") 
