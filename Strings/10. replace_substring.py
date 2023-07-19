# Question: Replace all occurrences of a substring in a string.
# Created by Devender Singh

def replace_substring(s, old, new):
    return s.replace(old, new)

# Driver code
input_str = "Hello, World!"
old_substring = "Hello"
new_substring = "Hi"
print("Modified string:", replace_substring(input_str, old_substring, new_substring))
