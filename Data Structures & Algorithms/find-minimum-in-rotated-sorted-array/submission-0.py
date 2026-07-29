class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        highh=len(nums)-1

        while low<high:
            mid=low+(high-low)//2


            # Minimum is in the right half
            if nums[mid]>nums[high]:
                low=mid+1

            else:
                high=mid

        return nums[low]            
        