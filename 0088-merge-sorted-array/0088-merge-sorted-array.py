class Solution(object):
    def merge(self, nums1, m, nums2, n):

        first = 0
        second = 0
        newarr = []

        while first < m and second < n:
            if nums1[first] <= nums2[second]:
                newarr.append(nums1[first])
                first += 1
            else:
                newarr.append(nums2[second])
                second += 1

        if first < m:
            newarr.extend(nums1[first:m])

        if second < n:
            newarr.extend(nums2[second:n])

        nums1[:] = newarr