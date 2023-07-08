# Question: Move all zeros to the end of an array while maintaining the order of non-zero elements.
# Created by Devender Singh

def move_zeros_to_end(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
            non_zero_index += 1

# Driver code
arr = [0, 2, 0, 5, 7, 0, 1, 0]
move_zeros_to_end(arr)
print("Array after moving zeros:", arr)
