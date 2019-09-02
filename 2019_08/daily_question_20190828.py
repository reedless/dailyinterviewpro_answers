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
    covered = []
    for interval in intervals:
        for i in range(interval[0]+1, interval[1]):
            if (i not in covered):
                covered.append(i)

    covered.sort()

    unique = []

    for i in range(len(covered)-1):
        if (not covered[i]+1 == covered[i+1]):
            unique.append(covered[i])
            unique.append(covered[i+1])
    unique.append(covered[-1])


    return unique

print (merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
