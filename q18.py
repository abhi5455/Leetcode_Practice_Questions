# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        current = head
        while current.next != None:
            new_node = ListNode(self.findGCD(current.val, current.next.val))
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        return head

    # Euclid’s Algorithm to find GCD
    def findGCD(self, a, b):
        while b:
            a, b = b, a % b
        return a

    # def findGCD(self, a, b):
    #     # num1, num2 = (a,b) if a < b else (b,a)
    #     num1, num2 = min(a,b) , max(a,b)
    #     num1Factors = [i for i in range(1,num1+1) if num1 % i == 0]
    #     gcd = 1
    #     for i in num1Factors:
    #         if (num2 % i ==0) and i > gcd:
    #             gcd = i
    #     return gcd