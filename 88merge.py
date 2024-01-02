class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Add integers from nums2 to open spots in nums1
        for i in range(n):
            nums1[m+i] = nums2[i]
        # Sort list in increasing order
        nums1.sort()