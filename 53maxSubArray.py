class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize max_sum with the first value from nums
        max_sum = nums[0]
        cur_sum = 0
        for n in nums:
            # If sum is ever negative disregard and start over since 0 is always greater than a negative sum
            if cur_sum < 0:
                cur_sum = 0
            # Update the current sum
            cur_sum += n
            # Update max_sum
            max_sum = max(max_sum, cur_sum)
        return max_sum
