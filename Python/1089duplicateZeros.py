class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Count up the zeros in the list
        zeros = arr.count(0)
        n = len(arr)
        # Loop to iterate through the list in reverse
        for i in range(n - 1, -1, -1):
            # Check ensures we don't access elements outside the original length of the list
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            # Check if a zero is found in the original list
            if arr[i] == 0:
                # Decrement zero count
                zeros -= 1
                # Repeat check to see if we are still in the bounds of the original
                if i + zeros < n:
                    arr[i + zeros] = 0
