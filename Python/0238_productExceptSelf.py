class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Initialize output list and fill with 1s to the same length as nums
        output = [1] * len(nums)
        # Prefix product is the product of all the values that came before the current index
        prefix = 1
        # Move forwards and calculate
        for i in range(len(nums)):
            # Place prefix product in the output list for later
            output[i] = prefix
            prefix *= nums[i]
        # Postfix product is the product of all the values that came after the current index
        postfix = 1
        # Move backwards and calculate the postfix product
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the prefix by the postfix to calculate the final product
            output[i] *= postfix
            postfix *= nums[i]
        return output
