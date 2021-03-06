# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        result = []
        length = 0

        head = root
        while head:
            length+=1
            head = head.next

        quotient, remainder = length//k , length%k if length>k else 0

        # naive solution 52%
        head, curr = root, root
        counter = 0

        while curr:
            counter+=1
            if remainder:
                if counter>quotient:
                    temp = curr.next
                    curr.next = None
                    result.append(head)
                    head, curr = temp, temp
                    remainder-=1
                    counter=0
                    continue
            else:
                if counter>=quotient:
                    temp = curr.next
                    curr.next = None
                    result.append(head)
                    head, curr = temp, temp
                    counter=0
                    continue

            curr = curr.next

        for i in range(k-len(result)):
            result.append([])

        return result


