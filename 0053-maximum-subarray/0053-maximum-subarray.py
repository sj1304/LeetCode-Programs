class Solution(object):
    def maxSubArray(self, nums):
        curr_dp=nums[0]
        max_sum=nums[0]

        for i in range(1,len(nums)):
            curr_dp=max(nums[i],curr_dp+nums[i])
            max_sum=max(max_sum,curr_dp)

        return max_sum
        