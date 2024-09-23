class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(log n) time complexity is required which suggests using a binary search
        left, right = 0, len(nums)-1
        while left < right:
            # Calculate the middle index
            mid = left + (right - left) // 2
            # If the middle number is greater than the rightmost number then the minimum is in the right half
            if nums[mid] > nums[right]:
                # Adjust left index to look through the left side of the array
                left = mid + 1
            # If check failed then the minimum is in the left half
            else:
                # Adjust right index to look through the right side
                right = mid
        return nums[left]
