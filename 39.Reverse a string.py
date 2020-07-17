"""Reverse a string"""

txt = input("Enter a string:")
print("Reverse of string:", txt[::-1])


def Reverse_string(t):
    txt2 = ''
    for i in t:
        txt2 = i + txt2

    return txt2


print("Reverse of a string:", Reverse_string(txt))
