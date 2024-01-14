class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize the current maximum, current minimum, and the max_product to the 1st value in the array
        # Maximums and minimums need to be tracked since negative values would flip values and complicate things
        curr_max = curr_min = max_product = nums[0]
        # Loop starting at the 2nd position in since we already initialized to the 1st
        for i in range(1, len(nums)):
            # Create temporary variable to store the previous value of the current max
            temp = curr_max * nums[i]
            # Update curr_max
            curr_max = max(nums[i], temp, nums[i]*curr_min)
            # Update curr_min
            curr_min = min(nums[i], temp, nums[i]*curr_min)
            # Select the max between the previous max_product and curr_max
            max_product = max(max_product, curr_max)
        return max_product
