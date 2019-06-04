# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = set()
        current = head
        while current is not None:
            if current in nodes:
                return True
            nodes.add(current)
            current = current.next
        return False
        