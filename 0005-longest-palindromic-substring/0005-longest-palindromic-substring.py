class Solution(object):
    def longestPalindrome(self, s):
        f = 0
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                f = 1
                break
        if f == 1:
            longest = s[0]
            for length in range(len(s), 0, -1):
                for i in range(len(s) - length + 1):
                    substring = s[i:i + length]
                    if substring == substring[::-1] and len(substring) > len(longest):
                        longest = substring
            return longest
        else:
            return s