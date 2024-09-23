class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize left and right pointers to first 2 indexes from array
        left, right = 0, 1
        curr_max = 0
        # Loop until the right pointer reached the end of the list
        while right < len(prices):
            # Check if the price to the left is smaller than the price on the right
            if prices[left] < prices[right]:
                # Calculate the potential profit
                profit = prices[right] - prices[left]
                # Select the max profit between the current max and the calculated profit
                curr_max = max(curr_max, profit)
            # If the price on the left is larger than the one on the right then move the left pointer to the right
            # position
            else:
                left = right
            # Always move the right pointer along to the next index
            right += 1
        return curr_max
