'''
Given a string with the initial condition of dominoes, where:

. represents that the domino is standing still
L represents that the domino is falling to the left side
R represents that the domino is falling to the right side

Figure out the final position of the dominoes.
If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.

Example:
Input:  ..R...L..R.
Output: ..RR.LL..RR
'''

class Solution(object):
    def pushDominoes(self, dominoes):
        right = []
        left = []
        for i in range(len(dominoes)):
            if (dominoes[i] == 'R'):
                right.append(i)
            if (dominoes[i] == 'L'):
                left.append(i)

        result = ['.'] * len(dominoes)

        for i in range(len(dominoes)):
            if (right == [] and left == []):
                break
            for r in right:
                if (r+i < len(dominoes)):
                    if (result[r+i] == '.'):
                        result[r+i] = 'R'
                else:
                    right.remove(r)
                    
            for l in left:
                if (0 < l-i):
                    if (result[l-i] == '.'):
                        result[l-i] = 'L'
                    if (result[l-i] == 'R'):
                        result[l-i] = '.'
                        left.pop(0)
                        right.pop(0)
                else:
                    left.remove(l)

        return ''.join(result)

print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
