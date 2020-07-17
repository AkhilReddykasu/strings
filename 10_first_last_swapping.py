"""first and last letter swapping"""

txt = input("enter a text:")
def swap(t):
    i = len(t)
    mid = t[1:i-1]
    return t[-1] + mid + t[0]
print("after swapping:",swap(txt))