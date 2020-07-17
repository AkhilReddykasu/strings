"""Reverse words in a string"""

txt = input("Enter a string:")


def reverse_string(t):
    txt2 = txt.split()
    txt3 = ''
    for i in txt2:
        if txt3 == '':
            txt3 += i[::-1]
        else:
            txt3 = txt3 + ' ' + i[::-1]
    return txt3


print("Reversing each word in string:",reverse_string(txt))
