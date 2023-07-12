# Question: Find the majority element in an array (element occurring more than n/2 times).
# Created by Devender Singh

def find_majority_element(arr):
    count = 0
    candidate = None
    
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    # Check if the candidate is indeed the majority element
    count = 0
    for num in arr:
        if num == candidate:
            count += 1
    
    if count > len(arr) // 2:
        return candidate
    return None

# Driver code
arr = [2, 2, 3, 5, 2, 2, 6]
print("Majority element:", find_majority_element(arr))
