'''
Given two strings, determine the edit distance between them.

The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other.

For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).
'''

def distance(s1, s2):
    matches = []
    for candidate in s1:
        for i in range(len(s2)):
            if (candidate == s2[i]):
                if (not i in matches):
                    matches.append(i)
                    break
    #matches must be strictly increasing, remove larger number
    for i in range(len(matches) - 1):
        if (matches[i] > matches[i+1]):
            matches.pop(i)
    
    return len(s2) - len(matches)

print (distance('biting', 'sitting'))
# 2
print (distance('ga', 'wanting'))
# 6
