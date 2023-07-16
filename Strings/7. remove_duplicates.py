# Question: Remove duplicate characters from a string.
# Created by Devender Singh

def remove_duplicates(s):
    unique_chars = ""
    for char in s:
        if char not in unique_chars:
            unique_chars += char
    return unique_chars

# Driver code
input_str = "programming"
print("String after removing duplicates:", remove_duplicates(input_str))
