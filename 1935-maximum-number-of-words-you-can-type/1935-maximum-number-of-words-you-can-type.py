class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        text=text.split()
        count=0
        for word in text:
            if any(ch in word for bk in brokenLetters for ch in bk):
                count+=1
        output=len(text)-count
        return output

        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        