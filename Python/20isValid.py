class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # If the length of s is odd then it's not valid
        if len(s) % 2 != 0:
            return False
        # Map opening brackets to their specific closing bracket
        pmap = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for c in s:
            # If c is an opening bracket add it to the stack
            if c in pmap:
                stack.append(c)
            # If c is a closing bracket but there are no opening brackets in the stack return False
            elif c not in pmap and len(stack) == 0:
                return False
            # Pop the stack retrieve its value from the pmap
            # If the value from the pmap is not the same as c then s is not valid
            elif not pmap.get(stack.pop()) == c:
                return False
        # If there is nothing in the stack after for loop then s is valid
        if len(stack) == 0:
            return True
        else:
            return False

