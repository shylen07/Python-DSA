# Question: Count the number of triplets that form a geometric progression.
# Created by Devender Singh

def count_triplets(arr, r):
    count = 0
    potential = {}
    pairs = {}
    
    for num in arr:
        if num in pairs:
            count += pairs[num]
        
        if num in potential:
            if num * r in pairs:
                pairs[num * r] += potential[num]
            else:
                pairs[num * r] = potential[num]
        
        if num * r in potential:
            potential[num * r] += 1
        else:
            potential[num * r] = 1
    
    return count

# Driver code
arr = [1, 3, 9, 9, 27, 81]
r = 3
print("Number of triplets:", count_triplets(arr, r))
