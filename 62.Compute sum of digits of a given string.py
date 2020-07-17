"""compute sum of digits of a given string"""

str1 = input("Enter a string of numbers:")
sum1 = 0
for i in str1:
    sum1 += int(i)
print("Sum of digits of a given string:", sum1)
