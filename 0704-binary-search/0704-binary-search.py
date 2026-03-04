class Solution(object):
    def search(self, nums, target):
        l=0
        h=len(nums)-1
        while(l<=h):
            mid=(l+h)/2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                h=mid-1
            else:
                l=mid+1
        return -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        