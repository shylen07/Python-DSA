# Question: Find all the leaders in an array (an element is a leader if it's greater than all elements to its right).
# Created by Devender Singh

def find_leaders(arr):
    n = len(arr)
    leaders = [arr[n - 1]]
    max_right = arr[n - 1]
    
    for i in range(n - 2, -1, -1):
        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]
    
    return leaders[::-1]

# Driver code
arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", find_leaders(arr))
