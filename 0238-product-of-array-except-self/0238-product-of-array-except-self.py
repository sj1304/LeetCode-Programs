class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        preff=[1]*n
        suff=[1]*n

        for i in range(0,n-1):
            preff[i+1]=preff[i]*nums[i]

        for i in range(n-1,0,-1):
            suff[i-1]=suff[i]*nums[i]
        
        print(preff,suff)
        for i in range(0,n):
            preff[i]=preff[i]*suff[i]
        
        return preff
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        