# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        ptr = head
        while ptr.next != None:
            temp = ListNode(self.gcd(ptr.val, ptr.next.val))
            temp.next = ptr.next
            ptr.next = temp
            ptr = temp.next
        return head

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
