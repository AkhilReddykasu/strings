"""program to check whether a string starts with specified characters"""

txt = input("enter a string:")
i = input("enter a starting string:")
result = txt.startswith(i)
print("is text starting with:",i,":",result)