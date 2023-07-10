# Question: Sort an array in wave form (arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] ...).
# Created by Devender Singh

def sort_in_wave(arr):
    n = len(arr)
    arr.sort()
    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Driver code
arr = [10, 5, 6, 3, 2, 20, 100, 80]
sort_in_wave(arr)
print("Wave-form sorted array:", arr)
