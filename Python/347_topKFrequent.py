class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Dictionary to hold the count of each element
        count = {}

        # Initialize a list of lists up to length of nums for bucket sort
        # freq[i] will store the numbers that appear exactly i times in the list.
        freq = [[] for i in range(len(nums) + 1)]

        # For each number in nums
        for n in nums:
            # Increment the freq in the dictionary
            count[n] = count.get(n, 0) + 1
        # Bucket sort
        for n, c in count.items():
            # n is the number and c is the frequency
            # Store the number in cth index in freq
            freq[c].append(n)

        res = []
        # Loop through frequencies starting at the end
        for i in range(len(freq) - 1, 0, -1):
            # For each number with that frequency
            for n in freq[i]:
                # Append to list and check if we reached the required amount of elements
                res.append(n)
                if len(res) == k:
                    return res
