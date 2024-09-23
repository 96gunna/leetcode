# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        # Iterate through the list while current is not a null node
        while current:
            # Temporarily store the next node in the list
            next_node = current.next
            # Set the pointer to point to the previous node in the list
            current.next = prev
            # Update prev variable to hold the current node
            prev = current
            # Move on to the next node in the list
            current = next_node
        # Return prev after loop which should be the head of the reversed list
        return prev
