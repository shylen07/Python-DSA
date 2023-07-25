# Question: Check if a string is a valid palindrome ignoring non-alphanumeric characters.
# Created by Devender Singh

def is_valid_palindrome(s):
    alphanumeric = [char.lower() for char in s if char.isalnum()]
    return alphanumeric == alphanumeric[::-1]

# Driver code
input_str = "A man, a plan, a canal, Panama"
if is_valid_palindrome(input_str):
    print("Valid palindrome")
else:
    print("Not a valid palindrome")