"""Length of longest string"""

txt = "for every action there is equal and opposite reaction."


def longest_string(t):
    str1 = t.split()
    max_length = len(str1)
    print(str1)
    str2 = []
    for i in str1:
        str2.append(len(i))
    str2.sort(reverse=False)
    print("length of longest string:", str2[-1])
    max_len_string = str2[-1]
    for j in range(0,max_length):
        if len(str1[j]) >= max_len_string:
            return str1[j]

print("Longest string in a text:", longest_string(txt))
