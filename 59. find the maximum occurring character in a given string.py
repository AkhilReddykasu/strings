"""Find the maximum occurring character in a given string"""

txt = input("Enter a string to find the maximum occurring character in a string:")


def Max_Occuring(t):
    maximum = ''
    max1 = ''
    for i in t:
        if i not in maximum:
            maximum += i
        elif i == ' ':
            pass
        else:
            max1 += i

    return max1



print("Find the maximum occurring character in a given string:",Max_Occuring(txt))
