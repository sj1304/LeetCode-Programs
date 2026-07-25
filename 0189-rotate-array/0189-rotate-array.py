class Solution(object):
    def rotate(self, nums, k):

        length = len(nums)
        a = [0] * length

        for i in range(length):
            new_index = (i + k) % length
            a[new_index] = nums[i]

        nums[:] = a