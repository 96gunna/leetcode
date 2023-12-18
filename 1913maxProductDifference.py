class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        num1, num2, num3, num4 = nums[-1], nums[-2], nums[0], nums[1]
        return (num1*num2)-(num3*num4)