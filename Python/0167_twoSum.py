class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # The numbers array is sorted, so we can use a two pointer method and manipulate the left and right pointers
        # based on if the calculated sum is larger or smaller than the target
        left, right = 0, len(numbers)-1
        # Loop until the left pointer is equal to the right pointer
        while left < right:
            # Calculate the current sum
            curr_sum = numbers[left] + numbers[right]
            # If curr_sum is equal to the target value return left+1 and right+1 since they want 1 based indexing
            if curr_sum == target:
                return [left+1, right+1]
            # If curr_sum is larger than target decrement the right pointer
            if curr_sum > target:
                right -= 1
            # If curr_sum is smaller than target increment the left pointer
            else:
                left += 1
