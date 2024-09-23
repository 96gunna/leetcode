class productExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        // Create a result array with the same amount of elements as the passed nums array
        int[] result = new int[nums.length];
        int prefix = 1;
        // Loop forward through the array
        for (int i = 0; i < nums.length; i++) {
            // Place the current prefix product in the corresponding position in the result array
            result[i] = prefix;
            // Update prefix product with the current number
            prefix *= nums[i];
        }
        int postfix = 1;
        // Loop through the array in reverse
        for (int i = nums.length - 1; i > -1; i--) {
            // Multiply the value in the result array with the postfix product
            result[i] *= postfix;
            // Update the postfix product with the current number
            postfix *= nums[i];
        }
        return result;
    }
}