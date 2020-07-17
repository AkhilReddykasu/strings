"""count and display the vowels of a given text"""

txt = input("Enter a string:")
vowels = "aeiou"
vowels_in_txt = ''
count = 0
for i in txt:
    if i in vowels:
        count += 1
        if i not in vowels_in_txt:
            vowels_in_txt += i
print("Numbers of vowels in given text:",count)
print("vowels in a given text:",vowels_in_txt)






