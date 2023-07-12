# Question: Count the number of vowels in a string.
# Created by Devender Singh

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Driver code
input_str = "Hello World"
print("Number of vowels:", count_vowels(input_str))