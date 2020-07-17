"""find the first repeated character in a given string"""

txt = input("enter a string to find a repeated character:")

txt2 = ''
for i in txt:
    if i in txt2:
        print("Finding the first repeated character:",i)
        break
    else:
        txt2 += i
























































