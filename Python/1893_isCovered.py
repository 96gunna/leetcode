class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        for num in range(left, right + 1):
            is_covered = False
            for start, end in ranges:
                if start <= num <= end:
                    is_covered = True
                    break
            if not is_covered:
                return is_covered
        return True
