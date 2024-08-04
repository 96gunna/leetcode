class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)
        while i < len1 or j < len2:
            if i < len1:
                res.append(word1[i])
                i += 1
            if j < len2:
                res.append(word2[j])
                j += 1
        return ''.join(res)