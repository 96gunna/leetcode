class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Initialize left and right pointers
        left, right = 0, len(nums)-1
        # Use <= to chance arrays with a single element
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            # If target is found return index
            if nums[mid] == target:
                return mid
            # Check if left half of the array is sorted
            if nums[left] <= nums[mid]:
                # If the target is within the bounds of the left side then update the right pointer
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                # Otherwise update the left pointer to search the right side
                else:
                    left = mid + 1
            # If it gets to this else block then the right half is sorted
            else:
                # If the target is within bounds of the right side then update the left pointer
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                # Otherwise update the right pointer to search the left side
                else:
                    right = mid - 1
        # Target is not in the array if the while loop is exited so return -1
        return -1
