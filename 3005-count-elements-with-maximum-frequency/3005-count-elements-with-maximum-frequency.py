class Solution(object):
    def maxFrequencyElements(self, nums):
        c=[0]*(max(nums)+1)
        for i in nums:
            c[i]+=1
        
        c.sort()

        length=len(c)-1
        count=c[length]

        while(True):
            if(c[length]==c[length-1]):
                count+=c[length-1]
                length=length-1
            else:
                break
        
        return count

        """
        :type nums: List[int]
        :rtype: int
        """
        