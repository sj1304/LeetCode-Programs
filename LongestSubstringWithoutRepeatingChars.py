class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        start = 0               # start index of current window
        max_len = 0
        temp = ""

        for i in range(len(s)):
            # search backwards but only down to 'start' (inclusive)
            for j in range(i - 1, start - 1, -1):
                if s[i] == s[j]:
                    start = j + 1
                    break

            curr = s[start:i + 1]   # current window (includes s[i])
            if len(curr) > max_len:
                max_len = len(curr)
                temp = curr

        return max_len