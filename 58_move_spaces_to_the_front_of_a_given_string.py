"""move spaces to the front of a given string"""

txt = input("enter a string:")
i = int(input("enter spacing value:"))
txt1 = txt.rjust(i)
print(txt1)
