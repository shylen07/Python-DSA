# Question: Find the length of the longest consecutive sequence in an array.
# Created by Devender Singh

def longest_consecutive_sequence(arr):
    num_set = set(arr)
    max_length = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

# Driver code
arr = [100, 4, 200, 1, 3, 2]
print("Longest consecutive sequence length:", longest_consecutive_sequence(arr))
