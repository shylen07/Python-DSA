# Question: Find the kth smallest element in an array.
# Created by Devender Singh

import heapq

def kth_smallest(arr, k):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heap[0]

# Driver code
arr = [3, 1, 4, 2, 5]
k = 3
print(f"{k}th smallest element:", kth_smallest(arr, k))
