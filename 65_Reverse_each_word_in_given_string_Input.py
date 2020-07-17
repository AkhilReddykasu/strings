"""Reverse each word in given string Input """

txt = input("enter a string of words:")
def string_rev(t):
    str1 = " "
    for i in t:
        str1 += i[::-1]
    return str1
txt2 = txt.split()
print("reverse of string:",string_rev(txt2))



