class Solution {
    public int maxSubArray(int[] nums) {
        // Initialize maxSum to the first position in the array
        int maxSum = nums[0];
        // Set the currSum to 0
        int currSum = 0;
        for (int n : nums) {
            // If currSum is less than 0 disregard and start over
            if (currSum < 0) currSum = 0;
            // Add n to the current sum
            currSum += n;
            // Place the higher value between currSum and maxSum into maxSum
            maxSum = currSum > maxSum ? currSum : maxSum;
        }
        return maxSum;
    }
}