# Question: Rotate an array to the right by k steps.
# Created by Devender Singh

def rotate_array(arr, k):
    n = len(arr)
    k %= n
    reversed_arr = arr[::-1]
    first_part = reversed_arr[:k][::-1]
    second_part = reversed_arr[k:][::-1]
    rotated_arr = first_part + second_part
    return rotated_arr

# Driver code
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Rotated array:", rotate_array(arr, k))
