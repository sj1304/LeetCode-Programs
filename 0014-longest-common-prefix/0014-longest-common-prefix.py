class Solution(object):
    def longestCommonPrefix(self, strs):
        s = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(s) and j < len(strs[i]):
                if s[j] != strs[i][j]:
                    break
                j += 1
            s = s[:j]

        return s