class Solution(object):
    def nextPermutation(self, nums):
        length = len(nums) - 1
        pivot = -1

        # Step 1: Find pivot
        for i in range(length, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i - 1
                break

        # If no pivot, reverse entire array
        if pivot == -1:
            nums.reverse()
            return

        # Step 2: Find next greater element
        for i in range(length, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        # Step 3: Reverse suffix
        left = pivot + 1
        right = length

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1