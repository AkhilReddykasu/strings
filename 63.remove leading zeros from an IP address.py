"""Remove leading zeros from an IP address"""

ip_address = input("Enter the IP address:")


def IP(ip):
    zeroip = ".".join([str(int(i)) for i in ip.split(".")])
    return zeroip


print("Removing leading zeros in ip address:", IP(ip_address))
