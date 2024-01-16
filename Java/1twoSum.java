class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Initialize HashMap for one pass
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            // Calculate the difference between the target and the current number
            int diff = target - nums[i];
            // If the difference is already in the HashMap then we can return
            if (hashmap.containsKey(diff)) {
                return new int[]{hashmap.get(diff), i};
            }
            // If the previous check failed then we insert the current number and its index into the HashMap
            hashmap.put(nums[i], i);
        }
        // Return null if nothing is found
        // This should never happen since a solution is guaranteed
        return null;
    }
}