class twoSum2 {
    public int[] twoSum(int[] numbers, int target) {
        // Initialize left pointer to beginning index
        int left = 0;
        // Initialize right pointer to ending index
        int right = numbers.length - 1;
        while (left < right) {
            // Calculate the current sum
            int currSum = numbers[left] + numbers[right];
            // If the target is found return the pointers+1 since question wants base 1
            if (currSum == target) return new int[]{left+1, right+1};
            // If currSum is larger than the target decrement the right
            if (currSum > target) right--;
            // If currSum is smaller than the target increment the left
            else left++;
        }
        // This will never happen since a solution is guaranteed
        return null;
    }
}