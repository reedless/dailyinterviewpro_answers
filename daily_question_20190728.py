'''
Given a string, find the length of the longest substring without repeating characters.
'''

import queue

class Solution:
	def lengthOfLongestSubstring(self, s):
		longest = 0
		queue = []
		for c in s:
			if c not in queue:
				queue.append(c)
			else:
				while queue[0] != c:
					queue.pop(0)
				queue.pop(0)
				queue.append(c)

			if len(queue) > longest:
				longest = len(queue)

		return longest


print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
