class Solution(object):
    def reverseWords(self, s):
        # Remove extra spaces
        s = " ".join(s.split())

        s = list(s)

        # Reverse entire string
        self.reverse(s, 0, len(s) - 1)

        start = 0

        # Reverse each word
        for curr in range(len(s) + 1):
            if curr == len(s) or s[curr] == ' ':
                self.reverse(s, start, curr - 1)
                start = curr + 1

        return ''.join(s)

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1