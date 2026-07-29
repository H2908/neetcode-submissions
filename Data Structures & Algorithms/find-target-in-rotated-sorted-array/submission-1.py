class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = low + (high - low) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[low] <= nums[mid]:

                # Target lies in left sorted half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1

                # Search in right half
                else:
                    low = mid + 1

            # Otherwise right half is sorted
            else:

                # Target lies in right sorted half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1

                # Search in left half
                else:
                    high = mid - 1

        return -1