# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        '''
        # Solution 1 (iterative)
        pre, cur = head, head.next
        swappedEndNode = None  # keep the end of swapped list
        while pre and cur:
            # do the swapping
            pre.next = cur.next
            cur.next = pre

            if swappedEndNode: # link to swapped part
                swappedEndNode.next = cur
            else:   # for the first time of swapping
                head = cur

            swappedEndNode = pre

            # move two nodes at a time
            pre = pre.next
            if pre:
                cur = pre.next

        return head

        # Solution 2 (iterative), more consice
        link = ListNode(0)  # dummy node linking to first even node
        link.next = head.next
        odd = head

        while odd.next:
            # do the swapping
            even = odd.next
            temp = even.next
            even.next = odd
            if temp and temp.next:
                odd.next = temp.next
            else:
                odd.next = temp

            # move two nodes at a time
            odd = temp
            if not(odd): break

        return link.next
        '''

        # Solution 3 (recursive), much more consice
        if head is None or head.next is None:
            return head
        fnext = head.next
        fnnext = fnext.next
        fnext.next = head
        head.next = self.swapPairs(fnnext)
        return fnext

