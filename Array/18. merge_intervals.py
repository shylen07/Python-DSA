# Question: Merge overlapping intervals in an array.
# Created by Devender Singh

def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])
    
    return merged

# Driver code
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("Merged intervals:", merge_intervals(intervals))
