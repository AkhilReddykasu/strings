"""prog to remove a new line in python"""

txt = 'akhil reddy \n kasu bala'
def rem_newline(t):
    str1 = " "
    str1 = str1.join(t)
    return str1
txt1 = txt.split()
print("removing a new line:",rem_newline(txt1))
