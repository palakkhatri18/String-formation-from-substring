# Given a string s, the task is to check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
class Solution:
	def isRepeat(self, s):
            tmp = s + s
            # Check if the original string appears within the concatenated string, excluding the first and last position
            if s in tmp[1:-1]:
                return 1
            return 0