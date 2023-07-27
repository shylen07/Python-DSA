# Question: Implement the 'strstr' function to find a substring in a string.
# Created by Devender Singh

def strstr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

# Driver code
haystack = "hello world"
needle = "world"
print("Needle found at index:", strstr(haystack, needle))
