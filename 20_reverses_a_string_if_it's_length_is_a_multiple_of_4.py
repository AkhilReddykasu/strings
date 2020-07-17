"""revrse a sting if the length is multiple of 4"""


txt = input("enter a string:")
if len(txt) % 4 == 0:
    print("revrse of a stering:",txt[::-1])
else:
    print("string length is not a multiple of 4")