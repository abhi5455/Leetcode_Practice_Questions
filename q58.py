# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        curr = head
        count = 0
        while curr != None:
            curr = curr.next
            count += 1
        curr = head
        for i in range(count//2-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
