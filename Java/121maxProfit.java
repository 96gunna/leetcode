class Solution {
    public int maxProfit(int[] prices) {
        // Initialize variables
        int left = 0, right = 1, currMax = 0;
        // Loop while right is less than the total elements in the array
        while (right < prices.length) {
            // Check if the price on the left is smaller than the price on the right
            if (prices[left] < prices[right]) {
                // Calculate the potential profit
                int profit = prices[right] - prices[left];
                // Select the larger profit between the current max and previous line
                currMax = profit > currMax ? profit : currMax;
            } else {
                // Move left pointer over to right if left was larger than right
                left = right;
            }
            // Increment right pointer to move along array
            right++;
        }
        return currMax;
    }
}