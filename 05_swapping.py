"""swapping characters in string"""

txt = input("enter the txt:")

'''
def swap(t):
    i = len(t)
    if i % 2 == 0:
        mid = t[1:i - 1]
        return t[-1] + mid + t[0]
'''


def swap(t):
    return t[-1] + t[1:len(t) - 1] + t[0]


print("after swapping", swap(txt))
