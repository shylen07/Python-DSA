# Question: Find the intersection of two arrays.
# Created by Devender Singh

def find_intersection(arr1, arr2):
    intersection = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    
    return intersection

# Driver code
arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 2, 4, 6]
print("Intersection:", find_intersection(arr1, arr2))
