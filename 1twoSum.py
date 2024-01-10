class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Empty dictionary
        hashmap = {}
        # Use enumerate to have access to both the index and value from the list
        for i, n in enumerate(nums):
            diff = target - n
            # If the difference is already in the hashmap then you know that the target sum can be reached with
            # the current number and the difference
            if diff in hashmap:
                return [hashmap[diff], i]
            # If the difference is not in the hashmap add n as a key and i as a value
            hashmap[n] = i
        # A return outside the loop is unnecessary since a solution is guaranteed in the list
