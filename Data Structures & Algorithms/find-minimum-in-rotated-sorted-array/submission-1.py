class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2

            # Minimum is in the right half
            if nums[mid] > nums[high]:
                low = mid + 1

            # Minimum is at mid or in the left half
            else:
                high = mid

        return nums[low]