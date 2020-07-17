"""Remove duplicate characters of a given string"""

txt = input("enter a string to remove duplicate characters:")
txt1 = ''
for i in txt:
    if i not in txt1:
        txt1 +=i
    else:
        pass
print("Removing dupicate characters from a string:",txt1)