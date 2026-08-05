class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
    
        for i in range(len(s)-1,-1,-1):
            if(s[i]==" "):
                if(count==0):
                    continue
                else:
                    break
            count+=1
        return count

        """
        :type s: str
        :rtype: int
        """
        