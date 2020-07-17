'''print the following floating numbers upto 2 decimal places with a sign'''

from numpy import *
a = float(input("enter a float value:"))
print(sign(a))
print("float value upto two numbers:",'%.2f'%a)