from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Key is a tuple of all the characters
        # Value is a list of words that consist of the characters in the tuple
        anagrams = defaultdict(list)
        for s in strs:
            # Create a list to hold every letter of the alphabet
            count = [0] * 26
            for c in s:
                # ord() returns the numeric unicode value of the passed in char
                # c will always be a lower case letter
                # ord(c) - ord('a') gives a value of 0 to 25
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            # Use a tuple as a key for the dictionary
            anagrams[key].append(s)
        # Return the values as a list
        return list(anagrams.values())
