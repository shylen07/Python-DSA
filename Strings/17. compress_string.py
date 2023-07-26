# Question: Compress a string by replacing repeated characters with their count.
# Created by Devender Singh

def compress_string(s):
    compressed = ""
    count = 1
    
    for i in range(len(s)):
        if i == len(s) - 1 or s[i] != s[i + 1]:
            compressed += s[i] + str(count)
            count = 1
        else:
            count += 1
    
    return compressed if len(compressed) < len(s) else s

# Driver code
input_str = "aabcccccaaa"
print("Compressed string:", compress_string(input_str))
