# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self,head):

        curr = head
        prev = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next

        head2 = self.reverse(slow)

        head1 = head

        while head1 and head2:
            nex1 = head1.next
            nex2 = head2.next

            head1.next = head2
            head1  = nex1
            head2.next = head1
            head2 = nex2




        
        