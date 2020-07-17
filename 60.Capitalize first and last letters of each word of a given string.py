"""Capitalize first and last of each word of a given string"""

txt = input("Enter a string:")
print("Before Capitalizing of first and last of each word of a given string:",txt)

def capitalize(t):
    txt1 = t.split()
    txt2 = ''
    for i in txt1:
        n = len(i)
        if txt2 == '':
            cap = i[0].upper() + i[1:n - 1] + i[n - 1].upper()
            txt2 = txt2 + cap
        else:
            cap = i[0].upper() + i[1:n - 1] + i[n - 1].upper()
            txt2 = txt2 + ' ' + cap
    return txt2


print("After capitalizing of first and last letters of each word in a given string:",capitalize(txt))
