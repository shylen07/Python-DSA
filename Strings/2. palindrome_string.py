# Question: Check if a string is a palindrome.
# Created by Devender Singh

def is_palindrome(s):
    return s == s[::-1]

# Driver code
input_str = "madam"
print("Is palindrome:", is_palindrome(input_str))