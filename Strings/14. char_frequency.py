# Question: Count the frequency of characters in a string.
# Created by Devender Singh

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Driver code
input_str = "programming"
print("Character frequency:", char_frequency(input_str))