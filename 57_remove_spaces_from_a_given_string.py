"""Removing spaces from a string"""


txt = input("enter a string:")
def remove_spaces(t):
    str= ""
    for i in t:
        str = str + i
    return str
txt =txt.split()
print("removing space from a string:",remove_spaces(txt))