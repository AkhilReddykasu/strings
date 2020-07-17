"""find the first repeated word in a given string"""

txt = input("enter a string:")
txt1 = txt.split()
txt2 = ''
for i in txt1:
    if i in txt2:
        print("find the first repeated word in a given string:",i)
        break
    elif txt2 == '':
        txt2 += i
    else:
        txt2 = txt2 + ' ' + i


