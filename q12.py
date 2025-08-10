# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        length = 1
        ptr = head
        while ptr.next != None:
            length += 1
            ptr = ptr.next

        mid = 0
        if length%2 == 0:
            mid = length/2
        else:
            mid = (length - 1) / 2

        ptr = head
        for i in range(mid):
            ptr = ptr.next

        return ptr
