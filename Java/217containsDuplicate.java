class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        // Loop through each number in the array
        for (int n : nums) {
            // Return true if n is already in the set
            if (set.contains(n)) {
                return true;
            }
            // Add current n to the set
            set.add(n);
        }
        // If loop is exited then all values are unique
        return false;
    }
}