class Solution(object):
    def searchRange(self, nums, target):
        def binarySearch(nums,target,find_first):
            left,right=0,len(nums)-1
            result=-1
            while(left<=right):
                mid=(left+right)//2
                print(mid)
                if(nums[mid]==target):
                    result=mid
                    if find_first:
                        right=mid-1
                    else:
                        left=mid+1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return result
        
        first=binarySearch(nums,target,True)
        last=binarySearch(nums,target,False)
        return[first,last] if first!=-1 else[-1,-1]

        
        