class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        else:
            return (n & -n) == n
        # return (n & -n) == n and n != 0
