class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Use a set since it has an average time complexity of O(1) for insertion and element checks
        temp = set()
        for n in nums:
            # If the value is already in the set return true
            if n in temp:
                return True
            temp.add(n)
        # Exiting the loop signifies that no dupes were found
        return False
