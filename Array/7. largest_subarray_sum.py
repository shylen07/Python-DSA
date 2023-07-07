# Question: Find the largest subarray sum in an array.
# Created by Devender Singh

def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Driver code
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Largest subarray sum:", max_subarray_sum(arr))
