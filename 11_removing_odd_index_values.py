"""removing odd index values"""

txt = input("enter thr text:")
for i in range(0,len(txt)):
    if i % 2 == 0:
        print("Removing odd index values:",txt[i])