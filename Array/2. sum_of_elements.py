# Question: Calculate the sum of all elements in an array.
# Created by Devender Singh

def calculate_sum(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum

# Driver code
arr = [2, 4, 6, 8, 10]
print("Sum of elements:", calculate_sum(arr))
