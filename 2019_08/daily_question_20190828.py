'''
You are given an array of intervals - that is, an array of tuples (start, end).
The array may not be sorted, and could contain overlapping intervals.
Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since
(5, 8) and (4, 10) can be merged into (4, 10).
'''

def merge(intervals):
    i = 0
    while i < len(intervals):
        curr = intervals[i]
        j = i+1
        while j < len(intervals):
            next = intervals[j]
            if (curr[1] > next[0] or next[1] > curr[0]):
                intervals.pop(j)
                intervals.pop(i)
                left = min(curr[0], next[0])
                right = max(curr[1], next[1])
                intervals.append((left, right))
            j += 1
        i += 1
    return intervals

print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
