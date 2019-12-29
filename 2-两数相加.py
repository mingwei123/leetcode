# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        p = l1
        q = l2
        curr = head
        carry = 0

        while p or q:
            if p:
                x = p.val
            else:
                x = 0
            if q:
                y = q.val
            else:
                y = 0
            sum = carry + x + y
            carry = int(sum / 10.0)
            curr.next = ListNode(int(sum%10))
            curr = curr.next
            if p:
                p=p.next
            if q:
                q=q.next
        if carry >=1:
            curr.next = ListNode(carry)
        return head.next
        
