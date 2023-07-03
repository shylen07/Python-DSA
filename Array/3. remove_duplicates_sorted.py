# Question: Remove duplicates from a sorted array.
# Created by Devender Singh

def remove_duplicates_sorted(arr):
    if not arr:
        return []
    
    unique_array = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            unique_array.append(arr[i])
    return unique_array

# Driver code
sorted_arr = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
print("Unique array:", remove_duplicates_sorted(sorted_arr))
