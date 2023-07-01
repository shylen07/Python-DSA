# Question: Find the maximum element in an array.
# Created by Devender Singh

def find_max_element(arr):
    max_element = float('-inf')
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Driver code
arr = [3, 7, 1, 9, 5]
print("Max element:", find_max_element(arr))
