"""length of first 3 characters"""
txt = input("enter the string:")
txt1 = txt.split()
def srting_len(l):
    i = len(l)
    if i > 3:
        del l[3:i]
    else:
        pass
    return l
print("first three characters:",srting_len(txt1))
for x in txt1:
    print("len of 1st three:",len(x))