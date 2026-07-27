class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m - 1

        # Step 1: Find the correct row
        while low <= high:
            mid = low + (high - low) // 2

            # Target lies within the range of this row
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:

                # Step 2: Binary search within the row
                left = 0
                right = n - 1

                while left <= right:
                    mid_col = left + (right - left) // 2

                    if matrix[mid][mid_col] == target:
                        return True
                    elif matrix[mid][mid_col] < target:
                        left = mid_col + 1
                    else:
                        right = mid_col - 1

                return False  # Target not found in the selected row

            # Search in the upper half of rows
            elif target < matrix[mid][0]:
                high = mid - 1

            # Search in the lower half of rows
            else:
                low = mid + 1

        return False