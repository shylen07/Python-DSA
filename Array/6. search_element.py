# Question: Search for an element in a sorted array using binary search.
# Created by Devender Singh

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Driver code
sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
print("Element found at index:", binary_search(sorted_arr, target))
