class Solution(object):
    """
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
            right -= 1"""

    def reverseWords(self,s):
        words=s.split()
        first=0
        second=len(words)-1
        print(words)

        while(first<second):
            words[first],words[second]=words[second],words[first]
            first+=1
            second-=1
        
        return " ".join(words)















