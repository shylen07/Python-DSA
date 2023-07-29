# Question: Find the longest common prefix among an array of strings.
# Created by Devender Singh

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    common_prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(common_prefix) != 0:
            common_prefix = common_prefix[:-1]
            if not common_prefix:
                return ""
    
    return common_prefix

# Driver code
strings = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(strings))