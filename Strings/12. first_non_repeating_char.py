# Question: Find the first non-repeating character in a string.
# Created by Devender Singh

def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# Driver code
input_str = "programming"
result = first_non_repeating_char(input_str)
if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")
