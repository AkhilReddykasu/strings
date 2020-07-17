"""That accepts a string and calculate the number of digits and letters"""

txt = input("Enter a string:")
letters = 0
digits = 0
for i in txt:
    if i.isalpha():
        letters += 1
    elif(i.isnumeric()):
        digits +=1
    else:
        pass

print("Number of letters:",letters)
print("Number of digits:",digits)


















