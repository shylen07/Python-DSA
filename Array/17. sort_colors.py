# Question: Sort an array of 0s, 1s, and 2s in ascending order.
# Created by Devender Singh

def sort_colors(arr):
    count = [0] * 3
    for num in arr:
        count[num] += 1
    
    index = 0
    for i in range(3):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1

# Driver code
arr = [2, 0, 2, 1, 1, 0]
sort_colors(arr)
print("Sorted colors:", arr)
