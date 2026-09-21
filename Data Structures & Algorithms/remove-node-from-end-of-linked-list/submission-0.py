# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head):
        curr = head
        prev = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        head1 = self.reverse(head)
        curr = head1
        dummy = ListNode()
        dummy.next = head1
        curr = dummy
        nex = curr.next

        while n!=1:
            curr = curr.next
            nex = nex.next
            n-=1
        
        curr.next = nex.next

        head2 = self.reverse(dummy.next)

        return head2



        
        