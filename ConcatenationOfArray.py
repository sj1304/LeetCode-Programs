class Solution(object):
    def getConcatenation(self, nums):
        ans=nums
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        