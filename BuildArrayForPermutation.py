class Solution(object):
    def buildArray(self, nums):
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        