# Question: Check if two strings are anagrams.
# Created by Devender Singh

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Driver code
string1 = "listen"
string2 = "silent"
print("Are anagrams:", are_anagrams(string1, string2))