"""Reverse each word and reverse word again Input"""

txt = input("Enter a string:")


def rev_txt(t):
    t1 = t.split()
    t2 = ''
    for i in t1:
        if t2 == '':
            t2 +=i[::-1]
        else:
            t2 = t2 + ' ' + i[::-1]
    print("Reverse word:",t2)
    return t2[::-1]


print("reverse of each word and reverse word again:",rev_txt(txt))





