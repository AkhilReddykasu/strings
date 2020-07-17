"""Swapping comma and dot"""

txt = input("Enter a sting:")

def replace(str1):
    str1 = str1.replace(',','temp')
    str1 = str1.replace('.',',')
    str1 = str1.replace('temp', '.')
    return str1

print(replace(txt))






















