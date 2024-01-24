class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the array to ascending order to use a two pointer approach
        nums.sort()
        result = []
        # Loop through nums with i being the index and n being the value
        for i, n in enumerate(nums):
            # Skip the current iteration if the current element is the same as the previous element
            if i > 0 and n == nums[i-1]:
                continue
            # Initialize left and right pointers
            left, right = i + 1, len(nums)-1
            # Loop to find a pair that along with n sums to 0s
            while left < right:
                three_sum = n + nums[left] + nums[right]
                # If calculated sum is greater than 0 decrement right pointer
                if three_sum > 0:
                    right -= 1
                # If sum is lesser than 0 increment left pointer
                elif three_sum < 0:
                    left += 1
                # If sum is 0 add trio to the list
                else:
                    result.append([n, nums[left], nums[right]])
                    # Move along left pointer
                    left += 1
                    # While loop skips over duplicate values on the left
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
